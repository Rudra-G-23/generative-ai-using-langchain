from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5, max_tokens=20)
parser = StrOutputParser()

path = r"C:\Users\Rudra\Desktop\generative-ai-using-langchain\10-document-loaders\01-txt-loader\cricket.txt"

loader = TextLoader(path, autodetect_encoding=True)

docs = loader.load()

prompt = PromptTemplate(
    template="Give me summary of given {text}", input_variables=["text"]
)

chain = prompt | model | parser
response = chain.invoke({"text": docs[0].page_content})
print(response)
