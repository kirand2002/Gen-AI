from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

promt_template = ChatPromptTemplate.from_messages([
    ("system","you are a {subject} teacher, ansswer in 50 words"),
    ("user","{question}")
])


subjecct = input("enter the subject of teacher")

que = input("enter the question")

promt = promt_template.invoke({"subject": subjecct,"question":que})



model = "llama3.2:latest"

llm=ChatOllama(model=model)

res= llm.invoke(promt)

print(res.content)



