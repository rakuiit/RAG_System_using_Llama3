from langchain_community.llms import Ollama

llm=Ollama(model="llama3")
response=llm.invoke("why is  the sky blue?")

print(response)