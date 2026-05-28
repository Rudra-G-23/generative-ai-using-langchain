"""
This is not working.
Reason for api issues
Last Update: 28-05-2026
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")

# Replace 'qwen2.5:0.5b' with 'llama3.2:3b' if you need tool calling
llm = ChatOpenAI(
    model="qwen2.5:0.5b",
    temperature=0.0,
    base_url="https://ollama.com/api",
    api_key=api_key,
)

response = llm.invoke("What is the capital of India?")
print(response.content)
