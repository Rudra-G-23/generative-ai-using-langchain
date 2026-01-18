import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OLLAMA_API_KEY")

# Create LLM
model = ChatOpenAI(
    model="cogito-2.1:671b",
    openai_api_base="https://ollama.com/v1",
    timeout=30,
    max_retries=3,
    max_tokens=16
)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input = input("<|YOU|> ").strip()
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() in {'exist', 'stop'}:
        print(f"Existing chatbot...")
        break
    
    response = model.invoke(user_input)
    chat_history.append(AIMessage(content=response.content))
    print(f"<|ASST|> {response.content}\n")

print(chat_history)