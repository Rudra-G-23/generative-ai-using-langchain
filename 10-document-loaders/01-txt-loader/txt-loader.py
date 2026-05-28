from langchain_community.document_loaders import TextLoader

path = r"C:\Users\Rudra\Desktop\generative-ai-using-langchain\10-document-loaders\01-txt-loader\cricket.txt"

loader = TextLoader(path, autodetect_encoding=True)

docs = loader.load()

# print(docs)
# print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)