import json
from typing import Annotated

import requests
from langchain.agents import AgentType, initialize_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import InjectedToolArg, tool
from langchain_groq import ChatGroq
from rich import print


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f"https://v6.exchangerate-api.com/v6/c754eab14ffab33112e380ca/pair/{base_currency}/{target_currency}"

    response = requests.get(url)

    return response.json()


@tool
def convert(
    base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]
) -> float:
    """
    given a currency conversion rate this function calculates the target currency value from a given base currency value
    """

    return base_currency_value * conversion_rate


print(f"\n\n{'--' * 25} Convert Args Output {'--' * 25}\n")
print(convert.args)

print(f"\n\n{'--' * 25} Get Convert {'--' * 25}\n")
get_conversion_factor.invoke({"base_currency": "USD", "target_currency": "INR"})

convert.invoke({"base_currency_value": 10, "conversion_rate": 85.16})

# tool binding
llm = ChatGroq(model="llama-3.1-8b-instant")

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

messages = [
    HumanMessage(
        "What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd"
    )
]

print(f"\n\n{'--' * 25} Message {'--' * 25}\n")
print(messages)

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

print(f"\n\n{'--' * 25} AI Message {'--' * 25}\n")
print(ai_message.tool_calls)

for tool_call in ai_message.tool_calls:
    # execute the 1st tool and get the value of conversion rate
    if tool_call["name"] == "get_conversion_factor":
        tool_message1 = get_conversion_factor.invoke(tool_call)

        # fetch this conversion rate
        conversion_rate = json.loads(tool_message1.content)["conversion_rate"]

        # append this tool message to messages list
        messages.append(tool_message1)

    if tool_call["name"] == "convert":
        # fetch the current arg
        tool_call["args"]["conversion_rate"] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)

print(f"\n\n{'--' * 25} Print Message {'--' * 25}\n")
print(messages)


print(f"\n\n{'--' * 25} LLM Output {'--' * 25}\n")
print(llm_with_tools.invoke(messages).content)


print(f"\n\n{'--' * 25} Agent {'--' * 25}\n")
agent_executor = initialize_agent(
    tools=[get_conversion_factor, convert],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # using ReAct pattern
    verbose=True,  # shows internal thinking
)


user_query = "Hi how are you?"
response = agent_executor.invoke({"input": user_query})

print(f"\n\n{'--' * 25} Response {'--' * 25}\n")
print(response)
