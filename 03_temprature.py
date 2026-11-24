from langchain_ollama import ChatOllama

model = "llama3.2:latest"

temp = [0,0.5,1.5]

for i in temp:

        llm = ChatOllama(model = model,temperature = i)

        res = llm.invoke("what is ai answer in one line")

        print(f" temp : {i} , output {res.content}")
      
