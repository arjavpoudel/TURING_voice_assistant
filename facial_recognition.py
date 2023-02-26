import cv2
import os
import numpy as np
from chatbot import chatbot


# Define paths to the training images folder and the face detection cascade file
training_images_path = "your-training-images-filepath-here"
face_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# Load the face detection cascade classifier
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# Create lists to store the training images and their corresponding labels
training_images = []
training_labels = []

# Loop over the training images folder and preprocess each image
for filename in os.listdir(training_images_path):
    basename, ext = os.path.splitext(filename)
    if basename.split("-")[0].isdigit():
        label = basename.split("-")[0] 
    else: 
        continue
    image_path = os.path.join(training_images_path, filename)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        face_img = cv2.resize(image[y:y+h, x:x+w], (100, 100))
        training_images.append(face_img)
        training_labels.append(label)
    
training_labels = np.array(training_labels).astype(np.int32)


# Train the machine learning model on the preprocessed training images
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(training_images, training_labels)

# Create a dictionary of label names for display
labels_dict = {i: "{value}" for i in range(1, 119)}

# Capture video stream and perform facial recognition
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Preprocess face image
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (100, 100))

        # Recognize face using trained model
        label, confidence = recognizer.predict(face_img)

        # Draw bounding box and label on face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        name = labels_dict[label]
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) == ord('q'):
        break

#after quit key pressed, webcam window is destroyed and chatbot function is called.        
if name == "{value}":
    cap.release()
    cv2.destroyAllWindows()
    chatbot()





