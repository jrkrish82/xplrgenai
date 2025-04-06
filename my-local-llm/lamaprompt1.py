from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama2:7b")

response = llm.invoke("The first man on the moon was ...")
print(response)