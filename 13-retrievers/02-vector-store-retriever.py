from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

huggingface_embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

model = ChatGroq(model="llama-3.1-8b-instant")

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=huggingface_embedding_model,
    collection_name="embedding_model",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

results = retriever.invoke("what is langchain")

print("---" * 100)
for i, doc in enumerate(results):
    print(f"\n--- Result {i + 1} ---")
    print(doc.page_content)
print("---" * 100)
