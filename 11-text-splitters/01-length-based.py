from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

path = r"C:\Users\Rudra\Desktop\generative-ai-using-langchain\11-text-splitters\2605.23904.pdf"

loader = PyPDFLoader(path)

docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0, separator="")

result = splitter.split_documents(docs)

print(result[1].page_content)
