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
