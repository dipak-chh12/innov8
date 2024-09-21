from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.getenv('innov8')
GEMINI_API_KEY = os.getenv('AIzaSyChMw1oApj6z6EGSaJZKTcwZBArCI9NHUQ')

print(f"Secret Key: {SECRET_KEY}")
print(f"Gemini API Key: {GEMINI_API_KEY}")
