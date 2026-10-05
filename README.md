# Final Project: Emotion Detector Web Application

**Project Name**: Final Project

A Python and Flask-based web application that detects emotions (anger, disgust, fear, joy, sadness) from text using the Watson NLP EmotionPredict service.

## Project Structure

```
.
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── requirements.txt
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Features

- **Emotion Detection Package (`EmotionDetection`)**: Interacts with the Watson NLP EmotionPredict API to extract emotion scores and find the dominant emotion.
- **Error Handling**: Gracefully handles invalid or blank input (API status 400) by returning `None` values and displaying `"Invalid text! Please try again!"`.
- **Unit Testing (`test_emotion_detection.py`)**: Tests emotion predictions across multiple emotional tones using `unittest`.
- **Flask Server (`server.py`)**: Provides `/` to render the user interface and `/emotionDetector` for processing analysis requests.
- **PEP8 & Static Code Analysis**: 100% compliant with PEP8 style guidelines, achieving a perfect `10.00/10` PyLint score.

## Installation & Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run Unit Tests:
   ```bash
   python3 test_emotion_detection.py
   ```

3. Run Static Code Analysis:
   ```bash
   pylint server.py
   pylint EmotionDetection/emotion_detection.py
   ```

4. Start Flask Server:
   ```bash
   python3 server.py
   ```
   Open your browser at `http://localhost:5000/`.
