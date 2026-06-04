from app.chains.rag_chain import chain, retriever

while True:
    question = input("You :")
    if question in ["bye", "exit", "tata"]:
        print("Good Bye Master Wayne")
        exit()
    docs = retriever.invoke(question)
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    response = chain.invoke({
        "context": context,
        "question": question
    })

    print("\nBot:", response.content)