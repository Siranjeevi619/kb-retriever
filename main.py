from app.chains.rag_chain import chain, retriever
from app.chains.rag_graph import graph

while True:
    question = input("You:")
    if question in ["bye", "exit", "tata"]:
        print("Good Bye Master Wayne")
        exit()
        
    response =  graph.invoke({
        "question":question
    })
    
    print(
    "Bot:",
    response["response"],
    f"\nSource: {response['resource']}"
    )