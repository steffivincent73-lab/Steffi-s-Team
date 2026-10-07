import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def get_model():
    if not API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Create a .env file and add your Gemini API key."
        )

    try:
        from google import genai
        client = genai.Client(api_key=API_KEY)
        return client
    except ImportError:
        raise RuntimeError("Install the required package with: pip install -r requirements.txt")

def generate_text(prompt: str) -> str:
    client = get_model()
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        contents=prompt
    )
    return response.text
