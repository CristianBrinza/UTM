import os
import logging
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from functools import partial
import string
import traceback

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = '8164832299:AAEYFL6aAFrc9em2_CaFDxgkqE8hnv40VrA'
DATASET_PATH = 'dataset.csv'
TOKENIZER_PATH = 'tokenizer.pickle'
MODEL_PATH = 'chatbot_model.keras'
EMBEDDING_DIM = 256
LSTM_UNITS = 512
BATCH_SIZE = 32
EPOCHS = 400
TEST_SIZE = 0.2
MAX_VOCAB_SIZE = 10000

def load_dataset(path: str) -> pd.DataFrame:
    data = pd.read_csv(path, quotechar='"', engine='python', on_bad_lines='skip')
    if 'question' not in data.columns or 'answer' not in data.columns:
        raise ValueError("Invalid dataset format. Must contain 'question' and 'answer' columns.")
    data.dropna(subset=['question', 'answer'], inplace=True)
    return data

def preprocess_text(text: str) -> str:
    text = text.lower().strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def preprocess_data(data: pd.DataFrame):
    questions = [preprocess_text(str(q)) for q in data['question'].values]
    answers = [preprocess_text(str(a)) for a in data['answer'].values]
    answers = ['<start> ' + ans.strip() + ' <end>' for ans in answers]

    tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE, filters='')
    tokenizer.fit_on_texts(questions + answers)

    with open(TOKENIZER_PATH, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    question_seqs = tokenizer.texts_to_sequences(questions)
    answer_seqs = tokenizer.texts_to_sequences(answers)

    max_seq_length = max(
        max((len(seq) for seq in question_seqs), default=0),
        max((len(seq) for seq in answer_seqs), default=0)
    )
    if max_seq_length == 0:
        raise ValueError("No valid sequences. Check your dataset.")

    encoder_input_data = pad_sequences(question_seqs, maxlen=max_seq_length, padding='post')
    decoder_input_data = pad_sequences([seq[:-1] for seq in answer_seqs], maxlen=max_seq_length, padding='post')
    decoder_target_data = pad_sequences([seq[1:] for seq in answer_seqs], maxlen=max_seq_length, padding='post')
    decoder_target_data = np.expand_dims(decoder_target_data, -1)
    return encoder_input_data, decoder_input_data, decoder_target_data, tokenizer, max_seq_length

def build_model(vocab_size: int, embedding_dim: int, lstm_units: int, max_seq_length: int) -> Model:
    encoder_inputs = Input(shape=(max_seq_length,))
    enc_emb = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True)(encoder_inputs)
    encoder_lstm = LSTM(lstm_units, return_state=True, dropout=0.2, recurrent_dropout=0.2)
    _, state_h, state_c = encoder_lstm(enc_emb)
    encoder_states = [state_h, state_c]

    decoder_inputs = Input(shape=(max_seq_length,))
    dec_emb_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True)
    dec_emb = dec_emb_layer(decoder_inputs)
    decoder_lstm = LSTM(lstm_units, return_sequences=True, return_state=True, dropout=0.2, recurrent_dropout=0.2)
    decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
    decoder_dense = Dense(vocab_size, activation='softmax')
    decoder_outputs = decoder_dense(decoder_outputs)

    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model: Model, encoder_input_data: np.ndarray, decoder_input_data: np.ndarray,
                decoder_target_data: np.ndarray, epochs: int, batch_size: int):
    es = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)
    mc = ModelCheckpoint(MODEL_PATH, monitor='val_loss', save_best_only=True, verbose=1)

    model.fit(
        [encoder_input_data, decoder_input_data],
        decoder_target_data,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.2,
        callbacks=[es, mc],
        verbose=1
    )

def load_resources():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not found. Train the model first.")
    if not os.path.exists(TOKENIZER_PATH):
        raise FileNotFoundError("Tokenizer not found.")
    with open(TOKENIZER_PATH, 'rb') as handle:
        tokenizer = pickle.load(handle)
    model = load_model(MODEL_PATH)
    max_seq_length = model.input_shape[0][1]
    return model, tokenizer, max_seq_length

def generate_response(model: Model, tokenizer: Tokenizer, max_seq_length: int, input_text: str) -> str:
    user_input = preprocess_text(input_text)
    if not user_input.strip():
        return "I'm not sure how to respond."
    input_seq = tokenizer.texts_to_sequences([user_input])
    if len(input_seq[0]) == 0:
        return "I’m not sure how to respond. Could you please rephrase?"
    input_seq = pad_sequences(input_seq, maxlen=max_seq_length, padding='post')

    decoder_input = np.zeros((1, max_seq_length))
    decoder_input[0, 0] = tokenizer.word_index.get('<start>', 1)
    response = []
    try:
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
    except Exception as e:
        logger.error(f"Error in response generation: {traceback.format_exc()}")
        return "I encountered an error."
    final_response = ' '.join(response).strip()
    if not final_response:
        final_response = "I'm not sure how to respond."
    return final_response

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User started conversation: {update.effective_user.username}")
    await update.message.reply_text('Hello! I am your Luna-City assistant bot. How can I help you today?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User asked for help: {update.effective_user.username}")
    await update.message.reply_text('Ask me about attractions, local cuisine, or practical tips about Chisinau.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE, model: Model, tokenizer: Tokenizer, max_seq_length: int):
    user_message = update.message.text
    logger.info(f"Received message from {update.effective_user.username}: {user_message}")
    if not user_message.strip():
        await update.message.reply_text("Please enter a valid message.")
        return
    try:
        response = generate_response(model, tokenizer, max_seq_length, user_message)
        logger.info(f"Response to {update.effective_user.username}: {response}")
        await update.message.reply_text(response)
    except:
        logger.error("Error generating response", exc_info=True)
        await update.message.reply_text("I'm sorry, I couldn't process your request.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception handling update:", exc_info=context.error)
    if update and hasattr(update, 'message') and update.message:
        await update.message.reply_text("An unexpected error occurred. Please try again later.")

def main():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(TOKENIZER_PATH):
        logger.info("Model or tokenizer not found. Training...")
        data = load_dataset(DATASET_PATH)
        encoder_input_data, decoder_input_data, decoder_target_data, tokenizer, max_seq_length = preprocess_data(data)
        vocab_size = min(MAX_VOCAB_SIZE, len(tokenizer.word_index) + 1)
        (encoder_train, encoder_val, decoder_train, decoder_val,
         target_train, target_val) = train_test_split(
            encoder_input_data, decoder_input_data, decoder_target_data,
            test_size=TEST_SIZE, random_state=42
        )
        model = build_model(vocab_size, EMBEDDING_DIM, LSTM_UNITS, max_seq_length)
        train_model(model, encoder_train, decoder_train, target_train, epochs=EPOCHS, batch_size=BATCH_SIZE)
        model.save(MODEL_PATH)
        logger.info("Model trained and saved.")
    else:
        logger.info("Model and tokenizer found. Skipping training.")

    model, tokenizer, max_seq_length = load_resources()
    logger.info("Starting Telegram bot...")

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND,
                                     partial(handle_message, model=model, tokenizer=tokenizer, max_seq_length=max_seq_length))
    application.add_handler(message_handler)
    application.add_error_handler(error_handler)
    logger.info("Bot is running. Waiting for messages...")
    application.run_polling()

if __name__ == '__main__':
    main()
