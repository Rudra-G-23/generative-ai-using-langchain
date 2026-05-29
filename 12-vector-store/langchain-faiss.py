"""requires-python = ">=3.9,<3.11". But in our project had different version."""

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize Embedding Model
huggingface_embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Define Documents
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

# Initialize FAISS Vector Store
vector_store = FAISS.from_documents(
    documents=docs, embedding=huggingface_embedding_model
)

# View Documents & Embeddings
print("---" * 33)
print("Vector Store Dictionary:", vector_store.docstore._dict)

# Search with similarity score
print("---" * 33)
results = vector_store.similarity_search_with_score(
    query="Who is bowler among this?", k=2
)
for res, score in results:
    print(f"Content: {res.page_content} \nScore: {score}\n")

# Meta-data filtering
print("---" * 33)
filtered_results = vector_store.similarity_search_with_score(
    query="", filter={"team": "Chennai Super Kings"}
)
for res, score in filtered_results:
    print(f"CSK Doc: {res.page_content} \nScore: {score}\n")

# Delete document by ID
print("---" * 33)
# Note: You can find exact IDs from `vector_store.docstore._dict.keys()`
doc_ids = list(vector_store.docstore._dict.keys())
if doc_ids:
    target_id = doc_ids[0]
    vector_store.delete(ids=[target_id])
    print(f"Deleted Document ID: {target_id}")

# Optional: Save FAISS index locally
vector_store.save_local("faiss_index")
