from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_tokens=20)
parser = StrOutputParser()

url = "https://en.wikipedia.org/wiki/Swami_Vivekananda"
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template="Answer the question {question} based the {text}",
    input_variables=["question", "text"],
)

chain = prompt | model | parser

print(
    chain.invoke(
        {
            "question": "who is swami",
            "text": docs[0].page_content[:5000],
        }
    )
)
