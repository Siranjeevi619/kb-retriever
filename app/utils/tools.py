from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from app.chains.rag_chain import retriever


@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo for information not available in the knowledge base.
    Use this when you need current or external information to answer the user's question.
    """
    search_tool = DuckDuckGoSearchResults()
    response = search_tool.invoke(query)
    return response


@tool
def retrieve_documents(query: str) -> str:
    """Retrieve relevant documents from the local FAISS knowledge base.
    Use this to find information from the stored PDF documents to answer the user's question.
    """
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant documents found in the knowledge base."
    return "\n\n---\n\n".join(doc.page_content for doc in docs)


def save_tool(question, response, resource):
    """Save conversation history to chat_history.txt."""
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(
            f"\nQuestion: {question}\n"
        )

        file.write(
            f"Answer: {response}\n"
        )

        file.write(
            f"Source: {resource}\n"
        )

        file.write(
            "\n" + "=" * 50 + "\n"
        )