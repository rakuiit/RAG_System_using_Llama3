from flask import Flask
from langchain_community.llms import Ollama

app=Flask(__name__)

# llm=Ollama(model="llama3")

# response=llm.invoke("why is  the sky blue?")

# print(response)


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)