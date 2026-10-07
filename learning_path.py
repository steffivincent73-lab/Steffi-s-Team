from gemini_client import generate_text

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.
Organize it from beginner to intermediate to advanced.
Include suggested timeline, important concepts, practice activities,
and useful types of resources such as videos, articles, books, or documentation.

Topic:
{topic}
"""
    return generate_text(prompt)
