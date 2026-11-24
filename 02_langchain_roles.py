from langchain_ollama import ChatOllama

from langchain_core.messages import SystemMessage, HumanMessage

model = "llama3.2:latest"


llm = ChatOllama(model=model)

mess = [
    ("system","you are former"),
    HumanMessage("What is ai answer in one line")
]

res = llm.invoke(mess)

print(res.content)