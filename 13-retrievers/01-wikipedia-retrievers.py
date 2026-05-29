import requests
from langchain_community.retrievers import WikipediaRetriever

# Set a custom user agent for all requests
requests.utils.default_headers_setter = lambda: {
    "User-Agent": "MyLangChainApp/1.0 (contact@example.com)"
}

wiki_retriever = WikipediaRetriever(top_k_results=2, lang="en")

docs = wiki_retriever.invoke("What is atom")

print("---" * 100)
print(docs)
