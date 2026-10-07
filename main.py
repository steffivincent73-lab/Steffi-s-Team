from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

load_dotenv()

app = FastAPI(title="EduGenie - AI Learning Assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/process", response_class=HTMLResponse)
async def process(request: Request, task: str = Form(...), text: str = Form(...)):
    result = ""
    try:
        if task == "Explain":
            result = explain_topic(text)
        elif task == "QnA":
            result = answer_question(text)
        elif task == "Quiz":
            result = generate_quiz(text)
        elif task == "Summary":
            result = summarize_text(text)
        elif task == "Recommend Path":
            result = get_learning_recommendations(text)
        else:
            result = "Please select a valid task."
    except Exception as e:
        result = f"Error: {e}"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "task": task, "input_text": text}
    )

@app.post("/qa")
async def qa(text: str = Form(...)):
    return {"answer": answer_question(text)}

@app.post("/explain")
async def explain(text: str = Form(...)):
    return {"explanation": explain_topic(text)}

@app.post("/quiz")
async def quiz(text: str = Form(...)):
    return {"quiz": generate_quiz(text)}

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    return {"summary": summarize_text(text)}

@app.post("/learn/recommendations")
async def recommendations(text: str = Form(...)):
    return {"recommendations": get_learning_recommendations(text)}
