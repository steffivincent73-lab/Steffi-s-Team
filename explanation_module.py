from gemini_client import generate_text

def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.
Explain the following topic in simple language for a beginner.
Use a short definition, key points, a real-world example, and a simple conclusion.

Topic:
{topic}
"""
    return generate_text(prompt)
