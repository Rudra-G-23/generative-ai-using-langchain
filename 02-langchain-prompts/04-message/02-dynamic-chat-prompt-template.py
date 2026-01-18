from langchain_core.prompts import ChatPromptTemplate

# This not work like PromptTemplate 
# from langchain_core.messages import SystemMessage, HumanMessage
# chat_prompt = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} Expert"),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])

# Dynamic Prompt
chat_prompt = ChatPromptTemplate([
    ('system', "You are a helpful {domain} Expert"),
    ('human', "Explain in simple terms, what is {topic}")
])

prompt = chat_prompt.invoke({
    'domain': 'odisha famous singer',
    'topic': 'How to sing well'
})

print(prompt)