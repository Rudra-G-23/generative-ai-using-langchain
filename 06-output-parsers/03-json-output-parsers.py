import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
os.getenv("HUGGINGFACEHUB_API_TOKEN")

load_dotenv()
os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.1, max_tokens=20)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
You are a JSON generator.

Return ONLY valid JSON.
Do not write markdown.
Do not write explanation.

{format_instruction}

Topic: {topic}
""",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)
