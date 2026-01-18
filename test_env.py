# This piece of code help us to know 
# Weather the KEY is in the environment or not

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("OLLAMA_API_KEY"))
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
