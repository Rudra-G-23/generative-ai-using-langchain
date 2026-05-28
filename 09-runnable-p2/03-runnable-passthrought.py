from dotenv import load_dotenv
from langchain_classic.schema.runnable import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
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

joke_gen_chain = RunnableSequence(joke_prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(explain_prompt, model, parser),
    }
)


chain = RunnableSequence(joke_gen_chain, parallel_chain)
print(chain.invoke({"topic": "air"}))


chain.get_graph().print_ascii()
