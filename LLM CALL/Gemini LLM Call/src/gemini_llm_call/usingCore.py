import os
from google import genai
from dotenv import load_dotenv
import requests

load_dotenv();

api_key = os.getenv("GEMINI_API_KEY")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "What is Java?"
                }
            ]
        }
    ]
}
response = requests.post(
    url,
    headers=headers,
    json=payload
)

print(response.json())