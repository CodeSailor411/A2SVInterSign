import pickle
import cv2
import mediapipe as mp
import numpy as np
import pyttsx3

# Load the pre-trained model
with open('./model.p', 'rb') as f:
    model_dict = pickle.load(f)
model = model_dict['model']

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Define labels dictionary
labels_dict = {0: 'Good job', 1: 'fist', 2: 'ok', 3: 'love',4:'hello',5:'peace'}  # Update with correct labels

# Track the last spoken word
last_spoken_word = None

def calculate_finger_distances(landmarks):
    # Extracting x and y coordinates from landmarks
    x_coords = [landmark.x for landmark in landmarks]
    y_coords = [landmark.y for landmark in landmarks]
    
    # Flattening the coordinates into a single array (2D x 21 landmarks, each with x and y)
    data_aux = []
    for i in range(len(landmarks)):
        data_aux.append(x_coords[i])
        data_aux.append(y_coords[i])
    
    # Ensure data has the correct number of features
    return np.array(data_aux).reshape(1, -1)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    H, W, _ = frame.shape

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks and connections
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            # Extract features from landmarks
            landmarks = hand_landmarks.landmark
            data_aux = calculate_finger_distances(landmarks)

            # Ensure data_aux has the correct number of features
            if data_aux.shape[1] != 42:
                print(f"Feature dimension mismatch: {data_aux.shape[1]} features found")
                continue

            # Make prediction
            prediction = model.predict(data_aux)
            predicted_character = labels_dict.get(int(prediction[0]), "Unknown")

            # Draw bounding box and label
            x_coords = [int(landmark.x * W) for landmark in landmarks]
            y_coords = [int(landmark.y * H) for landmark in landmarks]
            x1, x2 = min(x_coords), max(x_coords)
            y1, y2 = min(y_coords), max(y_coords)

            cv2.rectangle(frame, (x1 - 10, y1 - 10), (x2 + 10, y2 + 10), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1 - 10, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

            # Speak out the predicted character if it is different from the last spoken word
            if predicted_character != last_spoken_word:
                tts_engine.say(predicted_character)
                tts_engine.runAndWait()
                last_spoken_word = predicted_character

    # Display the frame
    cv2.imshow('Sign Language Recognition', frame)

cap.release()
cv2.destroyAllWindows()
