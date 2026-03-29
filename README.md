

# Farmer Support ChatBot

## Overview

In this repository, you'll find a Flask backend (`chat.py`), a React frontend (`app.jsx`), and training scripts (`train.py`) for the machine learning model. The machine learning model is trained on agricultural intents to provide context-aware responses. The frontend offers an intuitive chat interface, supporting multiple languages and enhancing user interaction.

## Installation

To run the code in this project, ensure you have the following dependencies:

-   Python 3
-   Flask
-   React
-   Socket IO
-   SpeechRecognition (for speech recognition)
-   Googletrans (for language translation)

You can install the required Python packages using the following commands:

```bash
pip install flask flask-socketio speechrecognition googletrans==4.0.0-rc1
```

For the React frontend, navigate to the `frontend` directory and run:

```bash
npm install
```

  Navigate to the project directory:

```bash
cd Farmer-Support-ChatBot
```

 Run the Flask backend:

```bash
python chat.py
``` 

  Run the React frontend:

```bash
npm run build
npm run dev
```
 Open your browser and access `http://localhost:5173/` to interact with the Farmer Support ChatBot.
