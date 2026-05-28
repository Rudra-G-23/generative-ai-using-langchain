from dotenv import load_dotenv
from langchain_classic.schema.runnable import (
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=500)
parser = StrOutputParser()

report_prompt = PromptTemplate(
    template="Write a report on {topic}", input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="Write a summary on {text}", input_variables=["text"]
)

report_gen_chain = report_prompt | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, summary_prompt | model | parser),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)
print(final_chain.invoke({"topic": "trip with friends"}))

final_chain.get_graph().print_ascii()
