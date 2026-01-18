import os
import requests
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OLLAMA_API_KEY")

# Test API connection
# headers = {"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"}
# response = requests.get("https://ollama.com/api/tags", headers=headers, timeout=30)
# print("API works:", len(response.json()["models"]), "models found")

# Create LLM
model = ChatOpenAI(
    model="cogito-2.1:671b",
    openai_api_base="https://ollama.com/v1",
    timeout=30,
    max_retries=3,
    max_completion_tokens=32
)

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain")
]

response = model.invoke(message)
print(response.content)