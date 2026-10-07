from gemini_client import generate_text

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage for quick revision.
Keep the important ideas, remove repetition, and use simple language.
Use bullet points when appropriate.

Passage:
{text}
"""
    return generate_text(prompt)
