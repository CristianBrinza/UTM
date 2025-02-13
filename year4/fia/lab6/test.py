import os
import logging
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
import re
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from functools import partial

# Configure logging for detailed insight
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = '8164832299:AAEYFL6aAFrc9em2_CaFDxgkqE8hnv40VrA'  # Set your token
DATASET_PATH = 'dataset.csv'
TOKENIZER_PATH = 'tokenizer.pickle'
MODEL_PATH = 'chatbot_model.keras'

EMBEDDING_DIM = 256
LSTM_UNITS = 512
BATCH_SIZE = 64
EPOCHS = 300  # This is a maximum; useing EarlyStopping to end training earlier if no improvement
TEST_SIZE = 0.2
MAX_VOCAB_SIZE = 10000

def clean_text(text: str) -> str:
    # Normalize user input: lowercase, strip spaces, remove unnecessary punctuation
    text = text.lower().strip()
    text = re.sub(r'[\?\!\.,;:]+', '', text)  # remove punctuation
    return text

def load_dataset(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        logger.error("Dataset file not found.")
        raise FileNotFoundError("Dataset file not found.")
    try:
        # If your dataset is clean, you might not need on_bad_lines='skip'
        data = pd.read_csv(path, quotechar='"', on_bad_lines='skip', engine='python')
    except pd.errors.ParserError as e:
        logger.error(f"Error reading dataset: {e}")
        raise
    if 'question' not in data.columns or 'answer' not in data.columns:
        logger.error("Dataset must contain 'question' and 'answer' columns.")
        raise ValueError("Invalid dataset format.")
    data.dropna(subset=['question', 'answer'], inplace=True)
    logger.info("Dataset loaded successfully.")
    return data

def preprocess_data(data: pd.DataFrame):
    logger.info("Preprocessing data...")
    # Convert all to lowercase and clean
    data['question'] = data['question'].apply(lambda x: clean_text(str(x)))
    data['answer'] = data['answer'].apply(lambda x: x.strip())

    questions = data['question'].values
    answers = data['answer'].values

    # Add start/end tokens
    answers = ['<start> ' + ans.strip() + ' <end>' for ans in answers]

    tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE, filters='')
    tokenizer.fit_on_texts(np.concatenate((questions, answers)))
    with open(TOKENIZER_PATH, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        logger.info("Tokenizer saved.")

    question_seqs = tokenizer.texts_to_sequences(questions)
    answer_seqs = tokenizer.texts_to_sequences(answers)
    max_seq_length = max(
        max(len(seq) for seq in question_seqs),
        max(len(seq) for seq in answer_seqs)
    )

    encoder_input_data = pad_sequences(question_seqs, maxlen=max_seq_length, padding='post')
    decoder_input_data = pad_sequences([seq[:-1] for seq in answer_seqs], maxlen=max_seq_length, padding='post')
    decoder_target_data = pad_sequences([seq[1:] for seq in answer_seqs], maxlen=max_seq_length, padding='post')
    decoder_target_data = np.expand_dims(decoder_target_data, -1)

    logger.info(f"Max sequence length: {max_seq_length}, Vocab size: {len(tokenizer.word_index)+1}")
    return encoder_input_data, decoder_input_data, decoder_target_data, tokenizer, max_seq_length

def build_model(vocab_size: int, embedding_dim: int, lstm_units: int, max_seq_length: int) -> Model:
    logger.info("Building model...")
    encoder_inputs = Input(shape=(max_seq_length,), name='encoder_inputs')
    enc_emb = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True, name='encoder_embedding')(encoder_inputs)
    encoder_lstm = LSTM(lstm_units, return_state=True, name='encoder_lstm')
    _, state_h, state_c = encoder_lstm(enc_emb)
    encoder_states = [state_h, state_c]

    decoder_inputs = Input(shape=(max_seq_length,), name='decoder_inputs')
    dec_emb_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True, name='decoder_embedding')
    dec_emb = dec_emb_layer(decoder_inputs)
    decoder_lstm = LSTM(lstm_units, return_sequences=True, return_state=True, name='decoder_lstm')
    decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
    decoder_dense = Dense(vocab_size, activation='softmax', name='decoder_dense')
    decoder_outputs = decoder_dense(decoder_outputs)

    model = Model([encoder_inputs, decoder_inputs], decoder_outputs, name='seq2seq_model')
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    logger.info("Model compiled.")
    return model

def train_model(model: Model, encoder_input_data: np.ndarray, decoder_input_data: np.ndarray,
                decoder_target_data: np.ndarray, epochs: int, batch_size: int):
    logger.info("Starting model training with EarlyStopping...")
    # EarlyStopping: stops training if no improvement after X epochs (patience)
    # This helps "automate" the effective number of epochs
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    history = model.fit(
        [encoder_input_data, decoder_input_data],
        decoder_target_data,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.2,
        callbacks=[early_stopping],
        verbose=1
    )
    logger.info("Training completed.")
    return history

def load_resources():
    if not os.path.exists(MODEL_PATH):
        logger.error("Trained model not found.")
        raise FileNotFoundError("Trained model not found.")
    if not os.path.exists(TOKENIZER_PATH):
        logger.error("Tokenizer not found.")
        raise FileNotFoundError("Tokenizer not found.")
    with open(TOKENIZER_PATH, 'rb') as handle:
        tokenizer = pickle.load(handle)
        logger.info("Tokenizer loaded.")
    model = load_model(MODEL_PATH)
    logger.info("Model loaded.")
    max_seq_length = model.input_shape[0][1]
    return model, tokenizer, max_seq_length

def generate_response(model: Model, tokenizer: Tokenizer, max_seq_length: int, input_text: str) -> str:
    logger.info(f"Generating response for: {input_text}")
    user_input = clean_text(input_text)
    if not user_input.strip():
        return "I’m not sure how to respond."

    input_seq = tokenizer.texts_to_sequences([user_input])
    # If no known tokens in input, provide a fallback response
    if len(input_seq[0]) == 0:
        return "I’m not sure how to respond."

    input_seq = pad_sequences(input_seq, maxlen=max_seq_length, padding='post')
    decoder_input = np.zeros((1, max_seq_length))
    decoder_input[0, 0] = tokenizer.word_index.get('<start>', 1)
    response = []
    for i in range(max_seq_length):
        prediction = model.predict([input_seq, decoder_input], verbose=0)
        predicted_id = np.argmax(prediction[0, i, :])
        if predicted_id == 0:
            break
        word = tokenizer.index_word.get(predicted_id, '')
        if word == '<end>':
            break
        response.append(word)
        decoder_input[0, i+1] = predicted_id

    final_response = ' '.join(response).strip()
    if not final_response:
        final_response = "I’m not sure how to respond."
    logger.info(f"Response: {final_response}")
    return final_response

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Luna-City assistant bot (FIA_Cristian_Brinza_FAF_212). How can I help you today?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can ask me questions about Chisinau, for example:\n- 'What are some must-see attractions in Chisinau?' \n- 'Where can I find local cuisine?'")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE, model: Model, tokenizer: Tokenizer, max_seq_length: int):
    user_message = update.message.text
    if not user_message.strip():
        await update.message.reply_text("Please enter a valid message.")
        return
    try:
        response = generate_response(model, tokenizer, max_seq_length, user_message)
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Error generating response: {e}", exc_info=True)
        await update.message.reply_text("I'm sorry, I encountered a problem processing your request. Please try again.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling update:", exc_info=context.error)
    # Gracefully handle unexpected errors in the bot
    if isinstance(update, Update) and update.message:
        await update.message.reply_text("An unexpected error occurred. Please try again later.")

def main():
    # If model or tokenizer do not exist, train the model
    if not os.path.exists(MODEL_PATH) or not os.path.exists(TOKENIZER_PATH):
        logger.info("Preparing and training the model...")
        data = load_dataset(DATASET_PATH)
        encoder_input_data, decoder_input_data, decoder_target_data, tokenizer, max_seq_length = preprocess_data(data)
        vocab_size = min(MAX_VOCAB_SIZE, len(tokenizer.word_index) + 1)

        # Split data into train/validation sets (80/20 recommended)
        encoder_train, encoder_val, decoder_train, decoder_val, target_train, target_val = train_test_split(
            encoder_input_data, decoder_input_data, decoder_target_data, test_size=TEST_SIZE, random_state=42
        )

        model = build_model(vocab_size, EMBEDDING_DIM, LSTM_UNITS, max_seq_length)
        train_model(model, encoder_train, decoder_train, target_train, epochs=EPOCHS, batch_size=BATCH_SIZE)
        model.save(MODEL_PATH)
        logger.info("Model saved.")

    # Load trained resources
    model, tokenizer, max_seq_length = load_resources()
    logger.info("Starting Telegram bot...")

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))

    # Handle all text messages except commands
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, partial(handle_message, model=model, tokenizer=tokenizer, max_seq_length=max_seq_length))
    application.add_handler(message_handler)
    application.add_error_handler(error_handler)

    # Start long-polling
    application.run_polling()

if __name__ == '__main__':
    main()
