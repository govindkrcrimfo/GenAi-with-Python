from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser
)
load_dotenv()

model=ChatGroq(
    model="openai/gpt-oss-20b"
)

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
# filled_prompt=prompt.invoke({
#     "topic":"SpringBoot"
# })
# response=model.invoke(filled_prompt)
# parsedResponse=jsonParser.invoke(response1)

# ****** above three invoke can be chained 
#chaining
chain=prompt | model | jsonParser 
response=chain.invoke({
    "topic":"Spring Boot"
})

print(type(response))
print(response)