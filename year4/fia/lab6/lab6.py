import os
import logging
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from functools import partial
import string
import traceback

# ====================================================
# Configuration
# ====================================================
TELEGRAM_BOT_TOKEN = '8164832299:AAEYFL6aAFrc9em2_CaFDxgkqE8hnv40VrA'
DATASET_PATH = 'dataset.csv'
TOKENIZER_PATH = 'tokenizer.pickle'
MODEL_PATH = 'chatbot_model.keras'
EMBEDDING_DIM = 256
LSTM_UNITS = 512
BATCH_SIZE = 64
EPOCHS = 300
TEST_SIZE = 0.2
MAX_VOCAB_SIZE = 10000
DROPOUT_RATE = 0.2

# ====================================================
# Logging Configuration
# ====================================================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ====================================================
# GPU/Device Check
# ====================================================
devices = tf.config.list_physical_devices('GPU')
if devices:
    logger.info(f"GPU detected. Using GPU: {devices}")
else:
    logger.warning("No GPU detected. Training might be slow.")

# ====================================================
# Data Loading and Preprocessing Functions
# ====================================================

def load_dataset(path: str) -> pd.DataFrame:
    """
    Load the dataset from a given CSV path. The dataset must contain 'question' and 'answer' columns.
    """
    logger.info("Loading dataset...")
    try:
        data = pd.read_csv(path, quotechar='"', on_bad_lines='skip', engine='python')
        if 'question' not in data.columns or 'answer' not in data.columns:
            logger.error("Dataset must contain 'question' and 'answer' columns.")
            raise ValueError("Invalid dataset format.")
        data.dropna(subset=['question', 'answer'], inplace=True)
        logger.info("Dataset loaded successfully.")
        return data
    except pd.errors.ParserError as e:
        logger.error(f"Error reading dataset: {e}")
        raise


"""
This function preprocesses text by:
1. Lowercasing all characters.
2. Removing whitespace from the beginning and end.
3. Removing punctuation (e.g., periods, commas).
"""
def preprocess_text(text: str) -> str:
    """
    Preprocess a given text by lowercasing, stripping whitespace, and removing punctuation.
    """
    text = text.lower().strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

"""
This function processes the dataset to prepare it for model training:
- Cleans questions and answers.
- Converts text to numerical sequences using a tokenizer.
- Adds special start/end tokens to the answers.
- Pads sequences to make them the same length.
"""
def preprocess_data(data: pd.DataFrame):
    """
    Preprocess the dataset into tokenized and padded sequences suitable for training.
    Adds <start> and <end> tokens to answers.
    """
    logger.info("Preprocessing data...")

    # Convert questions and answers to strings and preprocess
    questions = [preprocess_text(str(q)) for q in data['question'].values]
    answers = [preprocess_text(str(a)) for a in data['answer'].values]

    # Add start/end tokens to answers
    answers = ['<start> ' + ans.strip() + ' <end>' for ans in answers]

    # Tokenizer
    tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE, filters='')
    tokenizer.fit_on_texts(questions + answers)

    # Save tokenizer for future inference
    with open(TOKENIZER_PATH, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    logger.info("Tokenizer saved.")

    question_seqs = tokenizer.texts_to_sequences(questions)
    answer_seqs = tokenizer.texts_to_sequences(answers)

    # Compute the maximum sequence length from both questions and answers
    max_seq_length = max(
        max((len(seq) for seq in question_seqs), default=0),
        max((len(seq) for seq in answer_seqs), default=0)
    )
    if max_seq_length == 0:
        logger.error("No valid sequences found. Check your dataset for empty entries.")
        raise ValueError("No valid sequences found.")

    # Prepare encoder and decoder inputs and targets
    encoder_input_data = pad_sequences(question_seqs, maxlen=max_seq_length, padding='post')
    decoder_input_data = pad_sequences([seq[:-1] for seq in answer_seqs], maxlen=max_seq_length, padding='post')
    decoder_target_data = pad_sequences([seq[1:] for seq in answer_seqs], maxlen=max_seq_length, padding='post')
    decoder_target_data = np.expand_dims(decoder_target_data, -1)

    logger.info(f"Max sequence length: {max_seq_length}")
    logger.info(f"Vocabulary size: {len(tokenizer.word_index)+1}")

    return encoder_input_data, decoder_input_data, decoder_target_data, tokenizer, max_seq_length


# ====================================================
# Model Functions
# ====================================================
def build_model(vocab_size: int, embedding_dim: int, lstm_units: int, max_seq_length: int) -> Model:
    """
    Build the Seq2Seq model using LSTM layers for both encoder and decoder.
    """
    logger.info("Building model...")

    # Encoder
    encoder_inputs = Input(shape=(max_seq_length,), name="encoder_input")
    enc_emb = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True, name="encoder_embedding")(encoder_inputs)
    enc_emb = Dropout(DROPOUT_RATE, name="encoder_dropout")(enc_emb)
    encoder_lstm = LSTM(lstm_units, return_state=True, dropout=DROPOUT_RATE, recurrent_dropout=DROPOUT_RATE, name="encoder_lstm")
    _, state_h, state_c = encoder_lstm(enc_emb)
    encoder_states = [state_h, state_c]

    # Decoder
    decoder_inputs = Input(shape=(max_seq_length,), name="decoder_input")
    dec_emb = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True, name="decoder_embedding")(decoder_inputs)
    dec_emb = Dropout(DROPOUT_RATE, name="decoder_dropout")(dec_emb)
    decoder_lstm = LSTM(lstm_units, return_sequences=True, return_state=True, dropout=DROPOUT_RATE, recurrent_dropout=DROPOUT_RATE, name="decoder_lstm")
    decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
    decoder_dense = Dense(vocab_size, activation='softmax', name="decoder_output")
    decoder_outputs = decoder_dense(decoder_outputs)

    model = Model([encoder_inputs, decoder_inputs], decoder_outputs, name="seq2seq_model")

    model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    logger.info("Model compiled.")
    model.summary(print_fn=logger.info)  # Log model summary
    return model


def train_model(model: Model,
                encoder_train: np.ndarray,
                decoder_train: np.ndarray,
                target_train: np.ndarray,
                epochs: int,
                batch_size: int):
    """
    Train the Seq2Seq model.
    """
    logger.info("Starting model training...")
    history = model.fit(
        [encoder_train, decoder_train],
        target_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.2
    )
    logger.info("Training completed.")
    logger.info(f"Final Training Loss: {history.history['loss'][-1]} | Final Training Accuracy: {history.history['accuracy'][-1]}")
    if 'val_loss' in history.history:
        logger.info(f"Final Validation Loss: {history.history['val_loss'][-1]} | Final Validation Accuracy: {history.history['val_accuracy'][-1]}")
    return history


def load_resources():
    """
    Load the trained model and tokenizer from disk.
    """
    if not os.path.exists(MODEL_PATH):
        logger.error("Trained model not found. Please train the model first.")
        raise FileNotFoundError("Trained model not found.")

    if not os.path.exists(TOKENIZER_PATH):
        logger.error("Tokenizer not found. Please ensure tokenizer is saved.")
        raise FileNotFoundError("Tokenizer not found.")

    with open(TOKENIZER_PATH, 'rb') as handle:
        tokenizer = pickle.load(handle)
        logger.info("Tokenizer loaded.")

    model = load_model(MODEL_PATH)
    logger.info("Model loaded.")
    max_seq_length = model.input_shape[0][1]
    return model, tokenizer, max_seq_length


# ====================================================
# Inference Functions
# ====================================================
def generate_response(model: Model, tokenizer: Tokenizer, max_seq_length: int, input_text: str) -> str:
    """
    Generate a response from the traine d model for a given input text.
    """
    logger.info(f"Generating response for user input: {input_text}")

    user_input = preprocess_text(input_text)
    if not user_input.strip():
        return "I'm not sure how to respond to that."

    input_seq = tokenizer.texts_to_sequences([user_input])
    if len(input_seq[0]) == 0:
        # Fallback if no known words
        return "I’m not sure how to respond. Could you please rephrase?"

    input_seq = pad_sequences(input_seq, maxlen=max_seq_length, padding='post')
    decoder_input = np.zeros((1, max_seq_length))
    # Start token
    start_idx = tokenizer.word_index.get('<start>', 1)
    decoder_input[0, 0] = start_idx

    response = []
    try:
        for i in range(max_seq_length):
            prediction = model.predict([input_seq, decoder_input], verbose=0)
            predicted_id = np.argmax(prediction[0, i, :])
            if predicted_id == 0:
                # Unknown token
                break
            word = tokenizer.index_word.get(predicted_id, '')
            if word == '<end>':
                break
            response.append(word)
            decoder_input[0, i+1] = predicted_id
    except Exception as e:
        logger.error(f"Error during inference: {traceback.format_exc()}")
        return "I encountered an error while processing your request."

    final_response = ' '.join(response).strip()
    if not final_response:
        final_response = "I’m not sure how to respond."
    logger.info(f"Model response: {final_response}")
    return final_response


# ====================================================
# Telegram Bot Handlers
# ====================================================
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User started conversation: {update.effective_user.username}")
    await update.message.reply_text('Hello! I am your Luna-City assistant bot. How can I help you today?')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User asked for help: {update.effective_user.username}")
    await update.message.reply_text('You can ask me questions about Luna-City. For example, ask about attractions, local cuisine, or travel tips.')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE, model: Model, tokenizer: Tokenizer, max_seq_length: int):
    user_message = update.message.text
    logger.info(f"Received message from {update.effective_user.username}: {user_message}")
    if not user_message.strip():
        await update.message.reply_text("Please enter a valid message.")
        return
    try:
        response = generate_response(model, tokenizer, max_seq_length, user_message)
        logger.info(f"Sending response to {update.effective_user.username}: {response}")
        await update.message.reply_text(response)
    except Exception:
        logger.error(f"Error generating response to {update.effective_user.username}: {traceback.format_exc()}")
        await update.message.reply_text("I'm sorry, I couldn't process your request.")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling update:", exc_info=context.error)
    if update and hasattr(update, 'message') and update.message:
        await update.message.reply_text("An unexpected error occurred. Please try again later.")


# ====================================================
# Main Execution
# ====================================================
def main():
    # Check if model and tokenizer exist, if not train
    if not os.path.exists(MODEL_PATH) or not os.path.exists(TOKENIZER_PATH):
        logger.info("Model or tokenizer not found. Starting training process...")
        # Load and print dataset content
        data = load_dataset(DATASET_PATH)
        logger.info("Printing all dataset entries (Q -> A):")
        for i, row in data.iterrows():
            logger.info(f"Q: {row['question']} -> A: {row['answer']}")

        encoder_input_data, decoder_input_data, decoder_target_data, tokenizer, max_seq_length = preprocess_data(data)
        vocab_size = min(MAX_VOCAB_SIZE, len(tokenizer.word_index) + 1)

        # Splitting data
        encoder_train, encoder_val, decoder_train, decoder_val, target_train, target_val = train_test_split(
            encoder_input_data, decoder_input_data, decoder_target_data, test_size=TEST_SIZE, random_state=42
        )
        logger.info(f"Data split: Train Size: {len(encoder_train)} Val Size: {len(encoder_val)}")

        model = build_model(vocab_size, EMBEDDING_DIM, LSTM_UNITS, max_seq_length)
        train_model(model, encoder_train, decoder_train, target_train, epochs=EPOCHS, batch_size=BATCH_SIZE)

        # Save the trained model
        model.save(MODEL_PATH)
        logger.info(f"Trained model saved at {MODEL_PATH}.")
    else:
        logger.info("Model and tokenizer found. Skipping training.")

    # Load model and tokenizer
    model, tokenizer, max_seq_length = load_resources()
    logger.info("Starting Telegram bot...")

    # Telegram application setup
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    message_handler = MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        partial(handle_message, model=model, tokenizer=tokenizer, max_seq_length=max_seq_length)
    )
    application.add_handler(message_handler)
    application.add_error_handler(error_handler)

    logger.info("Bot is running. Waiting for messages...")
    application.run_polling()


if __name__ == '__main__':
    main()
