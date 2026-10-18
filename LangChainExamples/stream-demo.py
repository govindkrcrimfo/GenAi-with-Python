from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(
        model="openai/gpt-oss-20b"
)

for chunks in model.stream(
    "write 20 lines poem about hard working man"):
    print(chunks.content , end=" " , flush=True)

