
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = "llama3.2:latest"

llm = ChatOllama(model=model)

chat_history = [
    SystemMessage(content="You are a friendly assistant.")
]

while True:

    prom = input("You: ")

    if prom.lower() == "bye":
        break

    # Store user message
    chat_history.append(HumanMessage(content=prom))

    # Send complete conversation
    res = llm.invoke(chat_history)

    # Store AI response
    chat_history.append(AIMessage(content=res.content))

    print("AI:", res.content)
