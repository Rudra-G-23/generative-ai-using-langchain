from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro"
)

output = model.invoke(
    "Tell me 5 things about Odisha"
)

print(output.content)