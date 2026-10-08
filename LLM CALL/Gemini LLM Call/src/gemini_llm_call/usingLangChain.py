import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

response=model.invoke("What is Java? Explain in 2 lines.")
print(response.content[0]["text"])