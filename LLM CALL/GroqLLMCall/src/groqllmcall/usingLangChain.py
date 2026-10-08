import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(
    model="openai/gpt-oss-20b"
)

response=model.invoke(" Write 2-3 lines about virat kohli")
print(response.content)