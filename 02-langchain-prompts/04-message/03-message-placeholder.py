from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
import os

# MessagesPlaceholder ≠ text history
# MessagesPlaceholder = structured message objects

BASE_FILE_PATH = os.getcwd()
CURRENT_FILE_PATH = "02-langchain-prompts/04-message/customer_support_chat_history.txt"
FILE_PATH = os.path.join(BASE_FILE_PATH, CURRENT_FILE_PATH)

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []

with open(FILE_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("Human:"):
            chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
        elif line.startswith("AI:"):
            chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))

prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print("\n\n", prompt)