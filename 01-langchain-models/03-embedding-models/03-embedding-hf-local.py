from langchain_huggingface import HuggingFaceEndpointEmbeddings

embedding = HuggingFaceEndpointEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    "Data is everywhere today is 14-10-2026 00:08 IST",
    "Night time, code, excited for langchain",
    "Thank you to nitish sir",
]

vector = embedding.embed_documents(docs)
print(str(vector))