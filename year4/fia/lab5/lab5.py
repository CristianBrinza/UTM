import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# For TensorFlow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# For accuracy calculation
from sklearn.metrics import accuracy_score

# Set the directory paths
data_dir = '/Users/cristianbrinza/Documents/GitHub/fia/lab5'
images_dir = os.path.join(data_dir, 'training')
labels_file = os.path.join(data_dir, 'labels.csv')

# Ensure the directory for saving images exists
output_dir = os.path.join(data_dir, 'data')
os.makedirs(output_dir, exist_ok=True)  # Creates the directory if it does not exist

def blur_image(image, kernel_size=(15, 15), sigma=10):
    """
    Applies Gaussian blur to the input image.

    Parameters:
    - image: Input image (numpy array).
    - kernel_size: Size of the Gaussian kernel (must be odd numbers).
    - sigma: Standard deviation for Gaussian kernel.

    The goal is to apply a blur that mimics a soft focus effect without completely distorting the image.
    """
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    return blurred

def sharpen_image(image):
    """
    Sharpens the input image using a custom kernel.

    The kernel highlights edges and fine details in the image by emphasizing differences between neighboring pixels.
    """
    # Refined sharpening kernel for stronger edge enhancement
    kernel_sharpening = np.array([[0, -1, 0],
                                  [-1, 5,-1],
                                  [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel_sharpening)
    return sharpened

def plot_blur_and_sharpen(image_path):
    """
    Reads an image, applies blur and sharpening, and plots the results.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image at {image_path} could not be loaded.")
        return

    # Convert image from BGR (OpenCV format) to RGB (Matplotlib format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    blurred_image = blur_image(image)
    blurred_image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
    sharpened_image = sharpen_image(image)
    sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

    # Plot original and blurred images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image_rgb)
    plt.title('Blurred Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Plot original and sharpened images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(sharpened_image_rgb)
    plt.title('Sharpened Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

def detect_face(image):
    """
    Detects a face in the image using Haar Cascade classifier.

    Parameters:
    - image: Input image (numpy array).

    Returns:
    - Tuple of (x, y, w, h) representing the face bounding box coordinates, or None if no face is detected.
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade classifier for face detection
    haar_cascade_path = 'haarcascade_frontalface_default.xml'

    # Check if the cascade file exists
    if not os.path.exists(haar_cascade_path):
        # Download the cascade file if not present
        import urllib.request
        url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
        urllib.request.urlretrieve(url, haar_cascade_path)
        print('Downloaded haarcascade_frontalface_default.xml')

    face_cascade = cv2.CascadeClassifier(haar_cascade_path)

    # Check if the cascade file is loaded correctly
    if face_cascade.empty():
        raise IOError('Unable to load the face cascade classifier xml file')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If no faces detected, return None
    if len(faces) == 0:
        return None
    else:
        # Since we assume only one face per image, return the first detected face
        # Each face is represented as (x, y, w, h)
        return faces[0]

def detect_eyes(image, face_coords):
    """
    Detects eyes within the detected face region.

    Parameters:
    - image: Input image (numpy array).
    - face_coords: Tuple of (x, y, w, h) representing the face bounding box.

    Returns:
    - List of eye coordinates [(ex, ey, ew, eh), ...]
    """
    x, y, w, h = face_coords
    roi_gray = cv2.cvtColor(image[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade classifier for eye detection
    haar_eye_cascade_path = 'haarcascade_eye.xml'

    # Check if the cascade file exists
    if not os.path.exists(haar_eye_cascade_path):
        # Download the cascade file if not present
        import urllib.request
        url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml'
        urllib.request.urlretrieve(url, haar_eye_cascade_path)
        print('Downloaded haarcascade_eye.xml')

    eye_cascade = cv2.CascadeClassifier(haar_eye_cascade_path)

    # Check if the cascade file is loaded correctly
    if eye_cascade.empty():
        raise IOError('Unable to load the eye cascade classifier xml file')

    # Detect eyes within face region
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # Adjust eye coordinates relative to the whole image
    eyes_adjusted = []
    for (ex, ey, ew, eh) in eyes:
        eyes_adjusted.append((x + ex, y + ey, ew, eh))

    return eyes_adjusted

def is_passport_photo(image):
    """
    Checks if the given image meets the passport photo requirements.

    Parameters:
    - image: Input image (numpy array).

    Returns:
    - acceptable: Boolean indicating if the photo is acceptable.
    - reasons: List of reasons if the photo is not acceptable.
    """
    acceptable = True
    reasons = []

    # Requirement 1: The photo should be colour
    if np.array_equal(image[:, :, 0], image[:, :, 1]) and np.array_equal(image[:, :, 1], image[:, :, 2]):
        acceptable = False
        reasons.append("The photo is not in color.")

    # Requirement 2: The photo should be in portrait orientation or square
    height, width = image.shape[:2]
    if height < width:
        acceptable = False
        reasons.append("The photo is not in portrait orientation or square.")

    # Requirement 3: The eyes of the subject should be at the same level (max error of 5 pixels)
    face_coords = detect_face(image)
    if face_coords is None:
        acceptable = False
        reasons.append("No face detected in the photo.")
    else:
        eyes = detect_eyes(image, face_coords)
        if len(eyes) < 2:
            acceptable = False
            reasons.append("Could not detect two eyes.")
        else:
            # Get the y-coordinate of the centers of the eyes
            eye_y_positions = [ey + eh // 2 for (ex, ey, ew, eh) in eyes[:2]]
            eye_y_diff = abs(eye_y_positions[0] - eye_y_positions[1])
            if eye_y_diff > 5:
                acceptable = False
                reasons.append("The eyes are not at the same level.")

    # Requirement 4: The photo should contain only one person
    # We can use the number of faces detected
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    haar_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(haar_cascade_path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) != 1:
        acceptable = False
        reasons.append("The photo does not contain exactly one person.")

    # Requirement 5: The head should represent 20% to 50% of the area of the photo
    if face_coords is not None:
        x, y, w, h = face_coords
        face_area = w * h
        image_area = width * height
        face_area_percentage = (face_area / image_area) * 100
        if not (20 <= face_area_percentage <= 50):
            acceptable = False
            reasons.append("The head does not represent 20% to 50% of the photo area.")
    else:
        acceptable = False
        reasons.append("No face detected to evaluate head size.")

    return acceptable, reasons

# Task 1: Plotting blur and sharpened images
# You can choose an image from your 'images' directory
sample_image_path = os.path.join(data_dir, 'images', 'passport_no_color.png')
plot_blur_and_sharpen(sample_image_path)

# Load labels from CSV file
print("Loading labels from CSV file...")
labels_df = pd.read_csv(labels_file, sep=',')

print("First few rows of labels_df:")
print(labels_df.head())

# Map True/False labels to 1/0 (case-insensitive and strip whitespace)
labels_df['label'] = labels_df['label'].astype(str).str.strip().str.lower().map({'true': 1, 'false': 0})

# Check for NaN values in labels
num_nan_labels = labels_df['label'].isna().sum()
if num_nan_labels > 0:
    print(f"Number of labels that could not be mapped: {num_nan_labels}")
    print("Unmapped labels:")
    print(labels_df[labels_df['label'].isna()])
    # Optionally drop rows with NaN labels
    labels_df = labels_df.dropna(subset=['label'])

# Function to load images and labels
def load_images_and_labels(labels_df, images_dir):
    images = []
    labels = []
    for index, row in labels_df.iterrows():
        # Adjust the image path to match the actual location
        image_filename = os.path.basename(row['new_path'])
        image_path = os.path.join(images_dir, image_filename)
        label = row['label']
        # Read and preprocess the image
        image = cv2.imread(image_path)
        if image is not None:
            # Resize images to a fixed size (e.g., 128x128)
            image = cv2.resize(image, (128, 128))
            images.append(image)
            labels.append(label)
        else:
            print(f"Warning: Image {image_path} could not be loaded.")
    images = np.array(images)
    labels = np.array(labels)
    return images, labels

# Load images and labels
print("Loading images and labels...")
images, labels = load_images_and_labels(labels_df, images_dir)
print(f"Total images loaded: {len(images)}")

if len(images) == 0:
    print("No images were loaded. Please check the image paths and labels.")
    exit(1)

# Split data into train (65%), temp (35%)
print("Splitting data into training, validation, and test sets...")
X_train, X_temp, y_train, y_temp = train_test_split(images, labels, test_size=0.35, random_state=42, stratify=labels)

# Further split temp into validation (20%) and test (15%)
val_size = 20 / (20 + 15)  # Proportion of temp to use for validation
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=1 - val_size, random_state=42, stratify=y_temp)

print(f"Train set size: {len(X_train)}")
print(f"Validation set size: {len(X_val)}")
print(f"Test set size: {len(X_test)}")

# Normalize images
X_train = X_train / 255.0
X_val = X_val / 255.0
X_test = X_test / 255.0

# Data generators (optional augmentation)
train_datagen = ImageDataGenerator(
    rotation_range=10,
    horizontal_flip=True,
    zoom_range=0.1
)

val_datagen = ImageDataGenerator()

# Create generators
train_generator = train_datagen.flow(X_train, y_train, batch_size=16)
val_generator = val_datagen.flow(X_val, y_val, batch_size=16)

# Define the CNN model
print("Building the CNN model...")
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Binary classification
])

# Compile the model
print("Compiling the model...")
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

# Early stopping and model checkpoint
callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
]

# Train the model
print("Training the model...")
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=50,
    callbacks=callbacks
)

# Predict on the test set
print("Evaluating the CNN model on the test set...")
y_pred_probs = model.predict(X_test)
y_pred = (y_pred_probs > 0.5).astype(int).reshape(-1)

# Calculate accuracy
cnn_accuracy = accuracy_score(y_test, y_pred)
print(f"CNN Model Test Accuracy: {cnn_accuracy * 100:.2f}%")

# Function to evaluate OpenCV-based system
def evaluate_opencv_system(X_test, y_test):
    correct = 0
    total = len(X_test)
    for i in range(total):
        image = (X_test[i] * 255).astype(np.uint8)
        acceptable, reasons = is_passport_photo(image)
        prediction = int(acceptable)
        if prediction == y_test[i]:
            correct += 1
        else:
            print(f"Misclassified image index {i}: True label={y_test[i]}, Predicted={prediction}")
            print(f"Reasons: {reasons}")
    opencv_accuracy = correct / total
    return opencv_accuracy

# Evaluate OpenCV-based system on the test set
print("Evaluating the OpenCV-based system on the test set...")
opencv_accuracy = evaluate_opencv_system(X_test, y_test)
print(f"OpenCV System Test Accuracy: {opencv_accuracy * 100:.2f}%")

# Print the results
print(f"CNN Model Test Accuracy: {cnn_accuracy * 100:.2f}%")
print(f"OpenCV System Test Accuracy: {opencv_accuracy * 100:.2f}%")
