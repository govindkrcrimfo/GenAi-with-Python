from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser
)
load_dotenv()

# StrOutputParser - converts LLM response to plain python text string(str)
strParser=StrOutputParser()

model=ChatGroq(
    model="openai/gpt-oss-20b"
)
response=model.invoke("Who is virat kholi in two lines ?")

parsedResponse=strParser.invoke(response)

print(parsedResponse)
print("************************************************************")


# JsonOuputParser - Converts LLM response to python dictionary.
jsonParser=JsonOutputParser()
prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system" , "Reply with json only , using keys  language , use , version "
        ),
        (
            "human" , "tell me about {topic} "
        )
    ]
)
filled_prompt=prompt.invoke({
    "topic":"SpringBoot"
})
response1=model.invoke(filled_prompt)

parsedResponse1=jsonParser.invoke(response1)

print(type(response1))
print(response1.content)

