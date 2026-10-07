# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant built with FastAPI,
HTML/CSS, and Google Gemini.

## Features

1. Question & Answer
2. Simple topic explanation
3. MCQ quiz generation
4. Educational text summarization
5. Personalized learning recommendations

## Project Structure

EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css

## Requirements

- Python 3.10+
- Google Gemini API key

## Installation

Open Command Prompt / Terminal inside the EduGenie folder.

### 1. Create a virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

### 2. Install dependencies

pip install -r requirements.txt

### 3. Configure Gemini

Copy `.env.example` and rename it to `.env`.

Then put your API key:

GEMINI_API_KEY=your_actual_key

### 4. Run the project

uvicorn main:app --reload

### 5. Open the application

http://127.0.0.1:8000

## API Endpoints

POST /qa
POST /explain
POST /quiz
POST /summarize
POST /learn/recommendations

## Notes

The project documentation supplied for this project describes Gemini for Q&A,
quiz generation, summarization and learning paths, and a lightweight local
explanation model. This implementation uses Gemini for all five functions so
the project can be installed and run more simply with one cloud API.
