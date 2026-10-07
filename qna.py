from gemini_client import generate_text

def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an academic question-answering assistant.
Answer the student's question accurately and concisely.
Use simple language and examples where useful.

Question:
{question}
"""
    return generate_text(prompt)
