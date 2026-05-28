import os

from dotenv import load_dotenv
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.1, max_tokens=300)

schema = [
    ResponseSchema(
        name="fact_1",
        description="Fact 1 about the topic",
    ),
    ResponseSchema(
        name="fact_2",
        description="Fact 2 about the topic",
    ),
    ResponseSchema(
        name="fact_3",
        description="Fact 3 about the topic",
    ),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me the 3 fact about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser
response = chain.invoke({"topic": "tiger"})
print(response)
