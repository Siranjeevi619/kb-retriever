from app.chains.rag_chain import retriever, chain
from app.utils.tools import web_tool, save_tool
from app.utils.state import State


def retreiver(State):
    docs = retriever.invoke(State['question'])
    return {"document": docs}


def route(State):
    documents = State['document']

    # Filter by relevance score threshold — as_retriever returns Documents,
    # but we need scores to filter. Switch to similarity_search_with_score:
    return "rag" if documents else "web"


def rag_node(State):
    document = "\n".join(doc.page_content for doc in State['document'])
    response = chain.invoke({
        "context": document,
        "question": State['question']
    })
    return {
        "response": response.content,
        "resource": "RAG"
    }


def web_node(State):
    response = web_tool(State['question'])
    return {
        "response": response,
        "resource": "web - search"
    }
    
    
def save_node(State):
    save_tool(State['question'], State['response'], State['resource'])
    return {
        "response":State['response'],
        "resource":State['resource']
    }
    