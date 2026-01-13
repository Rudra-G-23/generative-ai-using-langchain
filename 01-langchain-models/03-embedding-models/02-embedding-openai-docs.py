from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-generation-3-large",
    dimensions=16
)

docs = [
    "I live in Odisha",
    "I knew the Odia language",
    "Data is everywhere today is 14-10-2026 00:08 IST",
    "Night time, code, excited for langchain",
]

response = embedding.embed_documents(docs)
print(str(response))
