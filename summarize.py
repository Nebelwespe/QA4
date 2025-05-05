# summarize.py

from openai import OpenAI
from env_loader import OPENAI_API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text):
    """
    Summarize a block of text using GPT-4.
    Returns a concise 2–3 sentence summary.
    """
    if not text or len(text.strip()) < 20:
        return "Text too short to summarize."

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Summarize the following news article in 3 sentences:\n\n{text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error summarizing text: {e}"
