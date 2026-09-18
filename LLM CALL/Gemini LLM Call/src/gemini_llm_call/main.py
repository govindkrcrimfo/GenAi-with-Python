from google import genai
from dotenv import load_dotenv
import time

#  Load environment variables (retrieves GEMINI_API_KEY from your .env file)
load_dotenv()
#  Initialize the Google GenAI SDK client
client = genai.Client()

# client.models.generate_content is best for immediate, single-turn prompts
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="who is virat kohli ? give in max 2-3 lines"
)
print(response.text)

print(" ***********************************************")

# client.interactions.create manages continuous state/sessions and agentic planning
# Takes more time 
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a joke in 2 lines",
    generation_config={
        "thinking_level": "low"  # Speeds up simple requests
    }
)
print(interaction.output_text)