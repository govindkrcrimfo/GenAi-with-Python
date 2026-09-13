import os       #loads os environment variable
from dotenv import load_dotenv

# loads the project environment variables
load_dotenv()

api_key=os.getenv('API_KEY')
print(api_key)
