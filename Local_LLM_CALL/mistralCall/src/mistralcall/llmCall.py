import langchain
from langchain_ollama import ChatOllama
def main():
  model=ChatOllama(
     model="mistral:latest"
  )
  response=model.invoke("who is virat kohli ?")
  print(response.content)
if __name__ == "__main__":
    main()