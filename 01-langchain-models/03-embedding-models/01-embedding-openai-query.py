from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=16
)

response = embedding.embed_query(
    "My name is Rudra Prasad Bhuyan"
)

print(str(response))