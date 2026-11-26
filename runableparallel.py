from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

topic = "python"



llm = ChatOllama(model = "llama3.2:latest")

parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_template(
    "Explain {topic} in 30 words."
) | llm | parser

prompt2 = ChatPromptTemplate.from_template(
    "Explain {topic} in 30 words."
) | llm | parser

prompt3 = ChatPromptTemplate.from_template(
    "Explain {topic} in 30 words."
) | llm | parser

parallel = RunnableParallel(explain = prompt1,b = prompt2,c = prompt3)


res = parallel.invoke({"topic" : topic})

for k,v in res.items():
    print(f"{k} : \n {v}")
