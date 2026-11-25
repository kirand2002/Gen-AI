
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a {subject} teacher, answer in 50 words"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{question}")
])

chat_history = []

llm = ChatOllama(model="llama3.2:latest")

parser = StrOutputParser()

chain = chat_template | llm | parser


while True:

    que = input("You: ")

    if que.lower() == 'bye':
        break

    response = ''

    print("Assistant: ", end="", flush=True)

    for i in chain.stream({
        "subject": "Assistant",
        "question": que,
        "chat_history": chat_history
    }):

        print(i, end="", flush=True)

        response += i

    print()

    chat_history.append(HumanMessage(content=que))

    chat_history.append(AIMessage(content=response))
