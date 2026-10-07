@echo off
echo Starting EduGenie...
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
pause
