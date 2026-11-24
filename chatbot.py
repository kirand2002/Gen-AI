import ollama

model1 =  model1 = "llama3.2:latest"

mess =[ {
        "role":"syetem",
        "content":"you are a friendly assistent"
    }
]

while True:

    prom = input("you :")

    if prom == "bye" or prom == "Bye":
        break

    user_role = {
        "role" : "user",
        "content" :  prom
    }

    mess.append(user_role)

    response = ollama.chat(model = model1, messages = mess)

    response = response.message.content

    print("Assitent :" ,response)

    assis = {
        "role" : "Assistent",
        "content" : response
    }


    

