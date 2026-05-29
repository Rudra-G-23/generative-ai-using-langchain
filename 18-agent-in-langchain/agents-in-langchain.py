import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from rich import print
from rich.pretty import pprint

# Load environment variables
load_dotenv()

# Build the LLM with enough tokens to process a ReAct loop
llm = ChatGroq(model="llama-3.1-8b-instant", max_tokens=1024)

search_tool = DuckDuckGoSearchResults()


@tool
def get_weather_data(city: str) -> dict:
    """This function fetches the current weather data for a given city."""
    url = f"https://weatherstack.com{city}"
    response = requests.get(url)
    return response.json()


# 1. Create the modern agent graph directly using create_agent
# Note: You can pass a string template or system prompt directly here
agent_graph = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant. Use tools when necessary.",
    # debug=True,  # Replaces verbose=True to print detailed information about execution
)

# 2. Define the user request matching the new state dictionary schema
inputs = {
    "messages": [
        {
            "role": "user",
            "content": "Find the capital of Madhya Pradesh, then find its current weather condition",
        }
    ]
}

# 3. Stream or invoke the agent graph
print("\n--- Executing Agent ---")
for chunk in agent_graph.stream(inputs, stream_mode="updates"):
    pprint(chunk)
