import os
from typing import Literal

from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

load_dotenv()
os.getenv("GROQ_API_KEY")


class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="Give me the sentiment of the feedback"
    )


model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=50)
pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)
str_parser = StrOutputParser()

classify_prompt = PromptTemplate(
    template="""Classify the text below into 'Positive' or 'Negative'. 

Strictly follow the format instructions. Ensure the 'sentiment' field is a single string value, not a list.

Text: {text}

Format Instructions:
{format_instruction}""",
    input_variables=["text"],
    partial_variables={"format_instruction": pydantic_parser.get_format_instructions()},
)

feedback_text_from_user = "useless phone, very slow, don't buy"

classifier_chain = classify_prompt | model | pydantic_parser

# response =  classifier_chain.invoke({"text": feedback_text_from_user}).sentiment
# print(response)

negative_prompt = PromptTemplate(
    template="Write a appropriate response to this Negative Feedback \n {feedback}",
    input_variables=["feedback"],
)

positive_prompt = PromptTemplate(
    template="Write a appropriate response to this Positive Feedback \n {feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", positive_prompt | model | str_parser),
    (lambda x: x.sentiment == "Negative", negative_prompt | model | str_parser),
    RunnableLambda(lambda x: "Couldn't found sentiment"),
)

chain = classifier_chain | branch_chain
response = chain.invoke({"text": feedback_text_from_user})
print(response)

# This show only which line is running
chain.get_graph().print_ascii()
