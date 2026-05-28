from langchain_community.document_loaders import PyPDFLoader

path = r"C:\Users\Rudra\Desktop\generative-ai-using-langchain\10-document-loaders\02-pypdf-loader\2605.23904.pdf"

loader = PyPDFLoader(path)

docs = loader.load()

# print(docs)

print(docs[0].page_content)
