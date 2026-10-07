from gemini_client import generate_text
import json
import re

def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def generate_quiz(passage: str) -> str:
    prompt = f"""
Create exactly 3 multiple-choice questions from the following educational text.
Return ONLY valid JSON in this format:
[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Educational text:
{passage}
"""
    raw = generate_text(prompt)
    try:
        data = json.loads(clean_json_block(raw))
        return json.dumps(data, indent=2)
    except Exception:
        return raw
