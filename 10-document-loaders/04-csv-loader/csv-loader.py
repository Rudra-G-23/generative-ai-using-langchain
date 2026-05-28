from langchain_community.document_loaders import CSVLoader

path = r"C:\Users\Rudra\Desktop\generative-ai-using-langchain\10-document-loaders\04-csv-loader\social-media.csv"

loader = CSVLoader(file_path=path)

docs = loader.load()

print(len(docs))
print(docs[1])
