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
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import string

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = '8164832299:AAEYFL6aAFrc9em2_CaFDxgkqE8hnv40VrA'
DATASET_PATH = 'dataset.csv'
TOKENIZER_PATH = 'tokenizer.pickle'
MODEL_PATH = 'chatbot_model.keras'
MAX_SEQ_LENGTH = 20
VOCAB_SIZE = 10000

# Load and preprocess dataset
def load_and_preprocess_dataset(path):
    data = pd.read_csv(path)
    data.dropna(subset=['question', 'answer'], inplace=True)
    data['question'] = data['question'].str.lower().str.strip()
    data['answer'] = data['answer'].str.lower().str.strip()
    data['answer'] = '<start> ' + data['answer'] + ' <end>'
    return data

# Train tokenizer
def train_tokenizer(data, num_words):
    tokenizer = Tokenizer(num_words=num_words, oov_token='<unk>')
    tokenizer.fit_on_texts(data['question'].tolist() + data['answer'].tolist())
    with open(TOKENIZER_PATH, 'wb') as f:
        pickle.dump(tokenizer, f)
    return tokenizer

# Prepare data for model training
def prepare_training_data(data, tokenizer, max_len):
    questions = tokenizer.texts_to_sequences(data['question'])
    answers = tokenizer.texts_to_sequences(data['answer'])
    encoder_input = pad_sequences(questions, maxlen=max_len, padding='post')
    decoder_input = pad_sequences([a[:-1] for a in answers], maxlen=max_len, padding='post')
    decoder_target = pad_sequences([a[1:] for a in answers], maxlen=max_len, padding='post')
    return encoder_input, decoder_input, decoder_target

# Build Seq2Seq model
def build_seq2seq_model(vocab_size, max_len, embedding_dim=128, lstm_units=256):
    # Encoder
    encoder_inputs = Input(shape=(max_len,))# Input layer for the decoder
    enc_emb = Embedding(vocab_size, embedding_dim, mask_zero=True)(encoder_inputs)# Embedding layer
    encoder_outputs, state_h, state_c = LSTM(lstm_units, return_state=True)(enc_emb)# LSTM layer
    encoder_states = [state_h, state_c]# Initialize with encoder states

    # Decoder
    decoder_inputs = Input(shape=(max_len,))
    dec_emb = Embedding(vocab_size, embedding_dim, mask_zero=True)(decoder_inputs)
    decoder_lstm = LSTM(lstm_units, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
    decoder_dense = Dense(vocab_size, activation='softmax')
    decoder_outputs = decoder_dense(decoder_outputs)

    # Compile model
    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Train and save model
def train_model(data, tokenizer):
    encoder_input, decoder_input, decoder_target = prepare_training_data(data, tokenizer, MAX_SEQ_LENGTH)
    model = build_seq2seq_model(VOCAB_SIZE, MAX_SEQ_LENGTH)
    model.fit([encoder_input, decoder_input], decoder_target,
              batch_size=64, epochs=100, validation_split=0.2,
              callbacks=[EarlyStopping(patience=5), ModelCheckpoint(MODEL_PATH, save_best_only=True)])
    model.save(MODEL_PATH)

# Load model and tokenizer
def load_model_and_tokenizer():
    with open(TOKENIZER_PATH, 'rb') as f:
        tokenizer = pickle.load(f)
    model = load_model(MODEL_PATH)
    return model, tokenizer

# Generate response
def generate_response(model, tokenizer, input_text):
    input_seq = tokenizer.texts_to_sequences([input_text.lower()])
    input_seq = pad_sequences(input_seq, maxlen=MAX_SEQ_LENGTH, padding='post')
    state_values = model.layers[2].predict(input_seq)
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = tokenizer.word_index['<start>']
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = model.layers[3].predict([target_seq] + state_values)
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_word = tokenizer.index_word.get(sampled_token_index, '')
        if sampled_word == '<end>' or len(decoded_sentence.split()) > MAX_SEQ_LENGTH:
            stop_condition = True
        else:
            decoded_sentence += ' ' + sampled_word
            target_seq[0, 0] = sampled_token_index
            state_values = [h, c]
    return decoded_sentence.strip()

# Telegram bot handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! Ask me anything.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE, model, tokenizer):
    user_message = update.message.text
    response = generate_response(model, tokenizer, user_message)
    await update.message.reply_text(response)

# Main function
def main():
    data = load_and_preprocess_dataset(DATASET_PATH)
    tokenizer = train_tokenizer(data, VOCAB_SIZE)
    train_model(data, tokenizer)
    model, tokenizer = load_model_and_tokenizer()

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT, partial(handle_message, model=model, tokenizer=tokenizer)))
    application.run_polling()

if __name__ == '__main__':
    main()
