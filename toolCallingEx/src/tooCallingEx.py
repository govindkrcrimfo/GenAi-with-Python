import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(
    model="openai/gpt-oss-20b"
)

def multiply(a:int , b:int )-> int :
    """ Multply two two number and give the exact result """
    return a*b

def add(a:int , b:int )-> int :
    """ Add two number and return the result"""
    return a+b

# Make both tools available to the LLM
model_with_tools=model.bind_tools([
    multiply, add
])

response=model_with_tools.invoke(
    "add 5 and 3 "
)

# Print the tool name and arguments selected by the LLM
# not tool executed yet only tool selected which need to call for the user query 
print("tool_called ",response.tool_calls)

