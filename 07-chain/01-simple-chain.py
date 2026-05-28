import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=50)

prompt = PromptTemplate(
    template="Generate a 2 interesting point about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser
response = chain.invoke({"topic": "chocolate"})
print(response)

chain.get_graph().print_ascii()
