import ollama

model1 = "llama3.2:latest"

messes = [
    {
        "role" : "system",
        "content" : "you are a funny former"
    },
    {
        "role" : "user",
        "content" : "what is ai"
    }
]

res = ollama.chat(model =model1 ,messages= messes)

print(res.message.content)