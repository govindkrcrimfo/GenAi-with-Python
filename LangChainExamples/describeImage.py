from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv();

model=ChatGroq(
    model="qwen/qwen3.8-27b"
)
image_url = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
url_message=HumanMessage(
   content=[
       {
           "type":"text",
           "text":"what is in this image describe in 2-3 lines"

       },
       {
           "type": "image_url",
           "image_url": {
                "url": image_url
            }
       }
   ]
)
resopnse=model.invoke([url_message])
print(resopnse.content)