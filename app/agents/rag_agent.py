from langgraph.prebuilt import create_react_agent
from app.llm.llm import llm
from app.utils.tools import retrieve_documents
from app.utils.state import State


RAG_SYSTEM_PROMPT = (
    "You are a RAG (Retrieval-Augmented Generation) specialist agent. "
    "Your job is to answer the user's question using ONLY the documents retrieved from the knowledge base. "
    "Use the retrieve_documents tool to search the knowledge base, then provide a clear and accurate answer "
    "based on the retrieved content. If the retrieved documents don't contain relevant information, "
    "say so clearly. Do not make up information. "
    "You MUST use the retrieve_documents tool — do NOT attempt to answer from your own knowledge."
)

# Create the RAG react agent with the retrieve_documents tool
rag_react_agent = create_react_agent(
    model=llm.bind_tools([retrieve_documents]),
    tools=[retrieve_documents],
    prompt=RAG_SYSTEM_PROMPT,
)


def rag_agent_node(state: State) -> dict:
    """RAG agent node — invokes the react agent and returns the response."""
    try:
        result = rag_react_agent.invoke(
            {"messages": [("user", state["question"])]}
        )
        # Extract the final AI message content
        final_message = result["messages"][-1].content
    except Exception as e:
        # Fallback: call the tool directly if the agent fails
        from app.utils.tools import retrieve_documents as rd
        raw_result = rd.invoke(state["question"])
        final_message = f"Retrieved from knowledge base:\n{raw_result}"

    return {
        "rag_response": final_message,
    }
