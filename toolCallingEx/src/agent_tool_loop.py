import os 
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

#create the agents is going to manage the tool calling loop
from langchain.agents import create_agent

load_dotenv()

model=ChatGroq(
    model="qwen/qwen3.8-27b"
)

@tool
def add (a:int , b:int )-> int:
    """Add two number and return the result """
    return a +b 

@tool
def multiply(a:int , b:int)->int:
    """Multiply two numbers and return the exact result"""
    return a*b

#creating the agent with required info
agent=create_agent(
    model=model,
    tools=[
        add,
        multiply
    ],
    system_prompt=(
        "your are a helpful assistant."
        "Use the tool when they fit"
    ),
)
# Asking questions using agent 
result=agent.invoke({
    "messages":[
      {  
        "role": "user",
        "content":(
           "what is 2 plus 8 ,"
           "and what is 2 mulplied by 8 is "
        )
      }
    ]
})

print(result["messages"][-1].content)
