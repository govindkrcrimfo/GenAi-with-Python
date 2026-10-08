import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# call for first response 
first_response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "which player scored most century in ODI for India in cricket , just give name of that player  ",
        }
    ],
    model="openai/gpt-oss-20b",
)
playerName=first_response.choices[0].message.content
print(playerName)
print()
print("***************************************")

second_response = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content": f"tell me about this player in 4 line in bulllet point {playerName}"
        }
    ],
    model="openai/gpt-oss-20b",
)
print(second_response.choices[0].message.content)

