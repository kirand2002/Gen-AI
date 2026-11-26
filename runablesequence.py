from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


chat_template = ChatPromptTemplate.from_messages([
    ("system","you are a {subject} teacher, ansswer in 50 words"),
    ("user","{question}")
])

subjecct = input("enter the subject of teacher: ")

que = input("enter the question: ")


llm = ChatOllama(model = "llama3.2:latest")

parser = StrOutputParser()

#chain = chat_template | llm | parser

chain = RunnableSequence(chat_template,llm,parser)

res = chain.invoke({"subject" : subjecct , "question":que})

print(res)