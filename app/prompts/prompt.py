from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant.
    
    

    Context:
    {context}

    Question:
    {question}
    """
)