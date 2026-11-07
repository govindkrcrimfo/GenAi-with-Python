import os
import sys
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq

load_dotenv()
# Support UTF-8 characters in the console
sys.stdout.reconfigure(encoding="utf-8")

model=ChatGroq(
    model="qwen/qwen3.8-27b"
)
@tool
def multiply(a:int , b:int )-> int :
    """ Multply  two number and give the exact result """
    return a*b

@tool
def add(a:int , b:int )-> int :
    """ Add two number and return the result"""
    return a+b
@tool
def countWords(text:str)->int:
    """How many words in the sentence and return the result"""
    return len(text.split())

# Make both tools available to the LLM
model_with_tools=model.bind_tools([
    multiply, add,countWords
])

reply=model_with_tools.invoke(
    "add 2 and 3 and also multiply 5 and 10 "
)

# Print the tool name and arguments selected by the LLM
# not tool executed yet only tool selected which need to call for the user query 
print("tool_called ",reply.tool_calls)

# tool mapper 
tools={
    "multiply":multiply,
    "add":add,
    "countWords":countWords
}



for tool_call in reply.tool_calls:

        print("\nTool called:", tool_call["name"])
        print("Arguments:", tool_call["args"])

        selected_tool = tools[tool_call["name"]]

        result = selected_tool.invoke(tool_call["args"])

        print("Result:", result)


print("No tools called!")
print(reply.content)



# if reply.tool_calls:
#     tool_called=reply.tool_calls[0]
#     print("Tool called ", tool_called["name"])

#     print("agrs : ",tool_called["args"])

#     selected_tool=tools[tool_called["name"]]
#     result=selected_tool.invoke(tool_called["args"])
#     print("Total words in given sentence is = ",result)
# else:
#     print("Tool not called !!")
#     print(reply.content)



