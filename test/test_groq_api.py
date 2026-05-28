import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.getenv("GROQ_API_KEY")

# Initialize the Groq model
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_tokens=20)

# Invoke the model with a prompt
response = llm.invoke("what is money")
print(response.content)
