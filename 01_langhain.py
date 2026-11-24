from langchain_ollama import ChatOllama

model = "llama3.2:latest"

llm = ChatOllama(model=model)

res= llm.invoke("what is AI ?")

print(res.content)
