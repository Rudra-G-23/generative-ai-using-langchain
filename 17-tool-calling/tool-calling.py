from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from rich import print

load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b


print(f"\n\n {'--' * 25} Check Tool {'--' * 25}")
print(multiply.invoke({"a": 3, "b": 4}))


llm = ChatGroq(model="llama-3.1-8b-instant", max_tokens=20)
print(f"\n\n {'--' * 25} First Interaction {'--' * 25}")
print(llm.invoke("hi"))

llm_with_tools = llm.bind_tools([multiply])
print(f"\n\n {'--' * 25} 2nd Interaction {'--' * 25}")
print(llm_with_tools.invoke("Hi how are you"))

query = HumanMessage("can you multiply 3 with 1000")
messages = [query]
print(f"\n\n {'--' * 25} Multiple Checking Interaction {'--' * 25}")
print(messages)

result = llm_with_tools.invoke(messages)
messages.append(result)
print(f"\n\n{'--' * 25} LLM w/ tool {'--' * 25}")
print(messages)

tool_result = multiply.invoke(result.tool_calls[0])
print(f"\n\n{'--' * 25} LLM answer {'--' * 25}")
print(tool_result)

messages.append(tool_result)
print(f"\n\n{'--' * 25} Append answer print message {'--' * 25}")
print(messages)

print(f"\n\n{'--' * 25} Final Output {'--' * 25}")
print(llm_with_tools.invoke(messages))
