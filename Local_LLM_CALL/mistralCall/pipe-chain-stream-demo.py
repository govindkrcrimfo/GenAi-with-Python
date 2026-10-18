import langchain
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model=ChatOllama(
     model="mistral:latest"
  )

chain=(ChatPromptTemplate.from_messages([
    ("system" , "you are Indian stock analyser ,give your verdict bur or not with reason , keep your ansere in less than 6 lines"),
    ("human","{stock}")
])
| model )

for chunks in chain.stream (
  {
    "stock":"Bharat electronics limited (BEL)"
  }
):
  print(chunks.content , end=" ", flush=True)

