from flask import Flask,request
from langchain_community.llms import Ollama

app=Flask(__name__)

cached_llm=Ollama(model="llama3")




@app.route("/ai",methods=["POST"])
def aiPOST():
    print("post ai called")
    json_content=request.json
    query=json_content.get("query")
    print(f"query:{query}")

    response=cached_llm.invoke(query)
    print(response)
    
    response_answer=f"Answer: {response}"
    return response_answer


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)