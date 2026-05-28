from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", max_tokens=100)
parser = StrOutputParser()

linkedin_prompt = PromptTemplate(
    template="Generate a LinkedIn post about - {topic}", input_variables=["text"]
)

tweeter_prompt = PromptTemplate(
    template="Generate a Tweet post about - {topic}", input_variables=["text"]
)

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(tweeter_prompt, model, parser),
        "linkedin": RunnableSequence(linkedin_prompt, model, parser),
    }
)

chain = parallel_chain.invoke({"topic": "ai"})
print(chain)

print(chain["tweet"])
print(chain["linkedin"])


parallel_chain.get_graph().print_ascii()
