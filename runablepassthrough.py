from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough





llm = ChatOllama(model = "llama3.2:latest")

parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_template(
    "Explain {question} in 30 words."
) 
prompt2 = ChatPromptTemplate.from_template(
    "question: {question}\n answer: {answer} \n"

    "rate this from 1 to 10"

)

prompt3 = ChatPromptTemplate.from_template(
    "question: {question}\n answer: {answer} \n"
   
       "rate this from 1 to 10"
) 


explain_chain = prompt1 | llm | parser

parallel1 = RunnablePassthrough.assign(answer = explain_chain) | prompt2 | llm | parser

parallel2 = RunnablePassthrough.assign(answer = parallel1) | prompt3 | llm | parser


res = parallel2.invoke({"question" : "what is python"})


print(res)
