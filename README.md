# InterSign

InterSign is designed to assist the deaf and hard-of-hearing community by providing real-time sign language translation through AI-generated avatars. The application supports various contexts, including media & entertainment, education, and video calls messaging. InterSign operates as a desktop and mobile app that runs in the background, capturing any sound output from the device and translating it into sign language.


# How It Works
InterSign captures the audio output from the user's device and uses AI models to convert the audio into sign language. The translated sign language is then displayed using a generative AI avatar that overlays on top of other applications. This avatar can be moved around the screen, providing flexibility and ease of use.

In addition to translating audio to sign language, InterSign also enables users to communicate through sign language using their webcam. The application uses computer vision models to recognize the user's sign language gestures and convert them into speech, which is then output through the user's microphone. This bidirectional translation facilitates seamless communication between deaf and hearing individuals.

# Approximative Approach of the structure of the repo !
InterSign/
├── sign_language_to_text_to_speech
    ├──The-26-letters-and-10-digits-of-American-Sign-Language-ASL.png
    ├──collect_imgs.py
    ├──create_dataset.py
    ├──data.pickle
    ├──inference_classifier.py
    ├──model.p
    ├──model_metadata.p
    ├──train_classifier.py
├──speech_to_text_to_sign_language
    ├──A2SL
    ├──assets
    ├──templates
    ├──.DS_Store
    ├──README.md
    ├──db.sqlite3
    ├──manage.py
    ├──requirements.txt
    
├── README.md


# Speech To Sign Language 
A Web Application which takes in speech recording as input, converts it into text thus to sign language represented by avatar.

Front-end using HTML,CSS,JS.
Speech recognition API
Text Preprocessing.
Dataset Videos of 3D avatar (alphabet sign language and over 120 words).

# Prerequisites
Python >= 3.8
Download all required packages for python requirements
# Installation Guide:
These instructions will get you download the project and running on your local machine for development and testing purposes.

# Instructions
run the python file using the command "python manage.py runserver 3000". it shows localhost address (looks like this "server at http://127.0.0.1:8000/") run on browser. Sign up then login Click on mic button to record speech or even type text. Speech is going to processed and respective animated outputs are shown accordingly and it also support entered text manually.



Some screenshots of both main features: 
![Capture d'écran 2024-07-21 140211](https://github.com/user-attachments/assets/47b0490c-964a-4894-9121-3e551ca1c4d4)
![Capture d'écran 2024-07-21 140301](https://github.com/user-attachments/assets/65260a01-ffa6-4813-9975-04c973fd6dc4)
![Capture d’écran 2024-07-21 140356](https://github.com/user-attachments/assets/a1b0255d-8c05-4fd9-a95f-5fe05dd5136a)
![Capture d’écran 2024-07-21 140424](https://github.com/user-attachments/assets/cb66bb66-8d7f-4c7e-8f1a-a38be12871c4)
![Capture d’écran 2024-07-21 140445](https://github.com/user-attachments/assets/fba94e6e-0b0d-4fe0-abf5-1d0ed52b73a9)
![Capture d'écran 2024-07-21 140458](https://github.com/user-attachments/assets/ceb693f2-b19e-43ef-b8f8-e3d307a7e774)
