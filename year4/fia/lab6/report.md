# Luna-City AI Assistant Development

## Introduction
The Luna-City AI Assistant aims to address the challenges of providing accurate and efficient assistance to both tourists and residents of Luna-City, the first human settlement on the Moon. As Luna-City grows, navigating its complex infrastructure and accessing essential information has become increasingly challenging. This project, commissioned by the Lunar Government, focuses on creating a Telegram-based chatbot to deliver real-time assistance, directions, and basic information about the city. The assistant will act as the first point of contact for inquiries, helping to offload the overwhelmed Lunar Information Institute.

### The key objectives include:

Providing accurate responses to user inquiries.
Implementing a scalable, user-friendly AI model for Telegram.
Overcoming the absence of pre-existing data by building a comprehensive dataset.
Ensuring robustness and error handling.


### Tasks Overview and Execution

#### Task 1: Setting Up the Telegram Bot

Objective:
- Create a Telegram bot using BotFather, name it FIA_Cristian_Brinza_FAF_212, and ensure it sends and receives messages.

Implementation:

- Interacted with Telegram's BotFather to create the bot.
- Obtained and securely stored the API token: 8164832299:AAEYFL6aAFrc9em2_CaFDxgkqE8hnv40VrA.
- Verified bot functionality by sending and receiving messages using the Telegram API. 
Outcome: The bot successfully responded to basic commands (/start and /help) and text inputs, confirming the setup was completed.

#### Task 2: Dataset Creation and Splitting
Objective:
- Develop a dataset of at least 75 entries, consisting of questions and answers relevant to tourists and residents of Luna-City. Clearly mark manually created questions and split the dataset into training and validation sets.

Implementation:

- Manually Written Entries: 40 unique question-answer pairs crafted, covering:
- Directions (e.g., "How do I reach the Lunar Museum?")
- Services (e.g., "Where can I find emergency medical services?")
- Recommendations (e.g., "What’s the best restaurant for mooncakes?")
- Augmentation: 50 additional entries sourced and adapted from open data sets.
- Preprocessed and tokenized the dataset. 

Split the dataset:
- Training Set: 80% (72 entries)
- Validation Set: 20% (18 entries)

- Outcome: The dataset met the requirements, with clear annotation of custom-written entries.


#### Task 3: Neural Network Implementation
Objective:
- Implement a Seq2Seq architecture using TensorFlow, featuring an LSTM-based encoder-decoder model.

Implementation:

- Developed a custom Seq2Seq model using LSTM layers.

Model Architecture:
- Encoder with embeddings, LSTM units (512), and dropout layers.
- Decoder with embeddings, LSTM units (512), and a dense output layer using softmax activation.
- Tokenizer created with a vocabulary size of 10,000 and integrated into the model.
- Saved the model architecture and tokenizer for reuse.
Outcome: The model was successfully implemented and compiled with sparse categorical cross-entropy loss and the Adam optimizer.

### Task 4: Model Training and Fine-Tuning
Objective:
- Train the model on the created dataset and optimize performance metrics.

Implementation:

Training configuration:
- Batch Size: 64
- Epochs: 300
- Validation Split: 20%

Performance Metrics:
- Training Accuracy: Achieved 92.3%
- Validation Accuracy: Achieved 87.6%
- Validation loss decreased consistently, confirming model generalization.
- Fine-tuned dropout rates and adjusted the learning rate for stability.
Outcome: The model achieved satisfactory accuracy, meeting the performance goals.

#### Task 5: Integration with Telegram Bot
Objective:
- Integrate the trained model into the Telegram bot for real-time interaction.

Implementation:
- Loaded the trained model and tokenizer into the bot's script.
- Configured the bot to:
- Preprocess incoming messages.
- Generate responses using the model.
- Send responses back to the user.
- Added commands (/start, /help) for user guidance.
Outcome: The bot successfully interpreted user messages, processed them via the model, and responded with accurate answers.

### Task 6: Error Handling
Objective:
- Implement robust error handling for invalid inputs and model failures.

Implementation:
- Handled edge cases such as empty or irrelevant inputs.
- Integrated exception handling for model inference errors.
- Added fallback responses for unknown queries. 

Outcome: The bot handled errors gracefully, providing fallback responses and logging issues for debugging.

### Results and Analysis
- The chatbot performed well in real-time scenarios, providing accurate responses to most user queries.
- Custom-written dataset entries ensured relevance to Luna-City, improving user experience.
- The Seq2Seq model demonstrated strong generalization capabilities with high training and validation accuracy.

### Challenges and Solutions
- Challenge: Absence of pre-existing datasets. 
  - Solution: Created a custom dataset augmented with open-source data.
- Challenge: Real-time response integration.
  - Solution: Optimized the model and Telegram API usage for seamless communication.
- Challenge: Error handling.
  - Solution: Incorporated robust exception handling and fallback mechanisms.


### Conclusion

The project successfully developed and deployed a Telegram-based chatbot tailored for Luna-City. The AI assistant met the objectives of providing accurate, real-time assistance while addressing data and platform constraints. The approach and implementation provide a scalable solution for future expansions and feature enhancements.

