from dotenv import load_dotenv
from langchain_classic.schema.runnable import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=100)
parser = StrOutputParser()


def word_count(text):
    return len(text.split())


joke_prompt = PromptTemplate(
    template="Write a joke on - {topic}", input_variables=["topic"]
)

joke_gen_chin = RunnableSequence(joke_prompt, model, parser)

parallel_chain = RunnableParallel(
    {"joke": RunnablePassthrough(), "word_count": RunnableLambda(word_count)}
)

chain = RunnableSequence(joke_gen_chin, parallel_chain)
print(chain.invoke({"topic": "Donkey"}))

chain.get_graph().print_ascii()
