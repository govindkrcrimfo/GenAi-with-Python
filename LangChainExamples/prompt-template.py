from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate , HumanMessagePromptTemplate

load_dotenv()

model=ChatGroq(
    model="openai/gpt-oss-20b"
)

#Dyanmic prompt defined
prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system","your are {language} expert , keep answer under {limit} words"
        ),
        (
            "human","explain the {topic} for beginner"
        )
    ]
)
#prompt set
filledPrompt=prompt.invoke(
    {
        "language":"java",
        "limit":80,
        "topic":"Thread"

    }
)
response=model.invoke(filledPrompt)
print(response.content)