import os

from dotenv import load_dotenv
from langchain_classic.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

load_dotenv()
os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.1, max_tokens=300)


class Person(BaseModel):
    name: str = Field(description="Name of the Person")
    age: int = Field(gt=18, description="Age of the person")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="""
    Generate a fictional person from {place}. 
    
    Return ONLY valid JSON.
    Do not explain anything.
    Do not generate code. 
    
    {format_instruction}
    """,
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser
response = chain.invoke({"place": "uk"})
print(response)
