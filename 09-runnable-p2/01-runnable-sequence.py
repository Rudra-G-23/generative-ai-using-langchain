from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=100)
parser = StrOutputParser()

joke_prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

explain_prompt = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

chain = RunnableSequence(joke_prompt, model, parser, explain_prompt, model, parser)
print(chain.invoke({"topic": "air"}))

chain.get_graph().print_ascii()