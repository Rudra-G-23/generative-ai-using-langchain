import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-4-mini-instruct",
    task="text-generation",
    huggingfacehub_api_token=huggingface_api_key,
    max_new_tokens=20,
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Why love is important")
print(response)
