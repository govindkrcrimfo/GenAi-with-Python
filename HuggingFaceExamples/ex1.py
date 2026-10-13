from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

print("access token. " , load_dotenv())

#hugging face model config 
end_point=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.3
  
)
model=ChatHuggingFace(llm=end_point)
response=model.invoke("Explain the effect of AI on jobs in 2-4 lines")
print(response.content)

