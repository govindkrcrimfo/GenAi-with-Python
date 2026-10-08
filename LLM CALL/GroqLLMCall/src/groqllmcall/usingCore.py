import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "openai/gpt-oss-20b",
    "messages": [
        {
            "role": "user",
            "content": "What is Java?"
        }
    ]
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

result = response.json()

print(result["choices"][0]["message"]["content"])