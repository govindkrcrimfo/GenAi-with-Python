import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

@tool
def book_seat(name:str , seat:str)->str:
    """Book a seat in the class for a person."""
    return f" Seat {seat} booked for {name}"

agent=create_agent(
    model="openai:gpt-4o-mini",
    tools=[book_seat],
    system_prompt=("You help learners book a seat in the LangChain class."),
    # tells the agent to store the conversation after each step - save in application memory
    checkpointer=InMemorySaver() 
)

def ask(question,thread_id):
    result=agent.invoke({
        "messages":[{
            "role":"user",
            "content":question
        },
        ]
    },
    config={"configurable": {"thread_id": thread_id}},
    )
    print(f" {thread_id} Q: {question}")
    print(f"{thread_id}  A: {result['messages'][-1].content}")
    print()

ask("My is Govind kr ", thread_id="Govind")
ask("Book A5 seat in the class" ,thread_id="Govind")
ask("What is my seat number and my name",thread_id="Govind")
ask("What is my seat number and my name",thread_id="Sagar")

