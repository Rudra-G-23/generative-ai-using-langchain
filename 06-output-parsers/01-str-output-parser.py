import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

tem1 = PromptTemplate(
    template="Write a 5 line summary on {topic}", input_variables=["topic"]
)

tem2 = PromptTemplate(
    template="Write a joke on following text. /n {text}", input_variables=["text"]
)

prompt1 = tem1.invoke({"topic": "Black Whole"})
result1 = model.invoke(prompt1)

prompt2 = tem2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)

print(result2.content)
