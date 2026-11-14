import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool

load_dotenv()

hotel_price_per_day={
    "kolkata":3000,
    "delhi":5000,
    "bengaluru":6000
}



@tool
def ticket_price(city:str)->int:
    """Get the flight ticket price in rupees from Mumbai to a city."""
    flight_price={
        "kolkata":10000,
        "delhi":8000,
        "bengaluru":9000
    }
    return flight_price.get(city.lower(),6000)

@tool
def hotel_price(city: str, days: int) -> int:
    """Get the total hotel cost in rupees for a number of days in a city."""

    city = city.lower().strip()
    return days * hotel_price_per_day.get(city, 10000)

agent=create_agent(
    model="openai:gpt-4o-mini",
    tools=[ticket_price,hotel_price],
    system_prompt=(
        "You are a helpful trip planning assistant. "
        "Use the appropriate tools to calculate flight and hotel expenses. "
        "Never guess prices."
    )
)
question = "I want to go to Kolkata for 2 day from Mumbai. What is my total cost?"
print(" Q : ",question)
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
})
print("A : ",response["messages"][-1].content)