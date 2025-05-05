# env_loader.py

from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env file from same directory as script
dotenv_path = Path(__file__).resolve().parent / ".env"
print("Does .env exist?", os.path.exists(dotenv_path))  # Feedback

load_dotenv(dotenv_path=dotenv_path, override=True)

# Fetch and validate keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Debug print
if OPENAI_API_KEY:
    print("✅ OpenAI API Key loaded")
else:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

if NEWS_API_KEY:
    print("✅ News API Key loaded")
else:
    raise ValueError("❌ NEWS_API_KEY not found in .env")

if EMAIL_ADDRESS and EMAIL_PASSWORD and RECIPIENT_EMAIL:
    print("✅ Email credentials loaded")
else:
    raise ValueError("❌ One or more email env variables missing")
