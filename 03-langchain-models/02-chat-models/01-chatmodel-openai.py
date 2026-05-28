from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    max_completion_tokens=150,
)

output = model.invoke("Write an poem on Odisha")

print(output)
