import ollama

model_name = "llama3.2:latest"

res = ollama.generate(model=model_name,prompt="write program of factorial number")

print(res.response)

