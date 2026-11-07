
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()



@tool
def current_time(city: str) -> str:
    """Get the current time in a city."""

    zones = {
        "mumbai": "Asia/Kolkata",
        "london": "Europe/London",
        "new york": "America/New_York"
    }

    zone = zones.get(city.lower())

    if zone is None:
        return f"I do not know the timezone for {city}."

    return datetime.now(ZoneInfo(zone)).strftime(
        "%d %B %Y, %I:%M %p"
    )


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the exact result."""
    return a * b


# Put our tools into a list
tools = [current_time, multiply]

# Map tool names to actual Python tool objects
tools_by_name = {t.name: t for t in tools}


model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
).bind_tools(tools)


# Create the conversation
messages = [
    SystemMessage(
        content="You are a helpful assistant. Use the tools when they fit."
    ),
    HumanMessage(
        content="What time is it in Mumbai, and what is 98765 times 43210?"
    ),
]

step = 1

while True:

    response = model.invoke(messages)
    print("Tools Called : ",response.tool_calls)

    # Save the LLM response in conversation history
    messages.append(response)

    if not response.tool_calls:
        print("\nFinal answer:")
        print(response.content)
        break

    print(f"Step {step}: the model asked for {len(response.tool_calls)} tool call(s)")

    for call in response.tool_calls:

        # Find the actual tool using its name
        tool_to_run = tools_by_name[call["name"]]

        # Execute the tool and create a ToolMessage
        tool_message = tool_to_run.invoke(call)

        print(f"{call['name']}({call['args']}) -> {tool_message.content}")

        # Save the tool result in conversation history
        messages.append(tool_message)

    step += 1
