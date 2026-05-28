import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=100)

prompt1 = PromptTemplate(
    template="Generate summary on the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a joke on following text /n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
response = chain.invoke({"topic": "smile"})
print(response)

chain.get_graph().print_ascii()