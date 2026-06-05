from app.agents.supervisor import supervisor_node
from app.agents.rag_agent import rag_agent_node
from app.agents.web_agent import web_agent_node
from app.agents.response_agent import response_agent_node
from app.utils.node import save_node
from app.utils.state import State
from langgraph.graph import StateGraph, START, END


def route_after_supervisor(state: State) -> str:
    """Route to the appropriate agent(s) based on supervisor's decision."""
    decision = state.get("next_agent", "rag")
    if decision == "both":
        return "both"
    elif decision == "web":
        return "web"
    else:
        return "rag"


# Build the multi-agent graph
builder = StateGraph(State)

# Add all agent nodes
builder.add_node("supervisor", supervisor_node)
builder.add_node("rag_agent", rag_agent_node)
builder.add_node("web_agent", web_agent_node)
builder.add_node("response_agent", response_agent_node)
builder.add_node("save_node", save_node)

# START → Supervisor
builder.add_edge(START, "supervisor")

# Supervisor → conditional routing to agents
builder.add_conditional_edges("supervisor", route_after_supervisor, {
    "rag": "rag_agent",
    "web": "web_agent",
    "both": "rag_agent",      # When "both", go to RAG first, then Web
})

# RAG Agent → either Response Agent or Web Agent (if "both" was selected)
def route_after_rag(state: State) -> str:
    """After RAG, go to Web Agent if 'both' was selected, otherwise to Response Agent."""
    if state.get("next_agent") == "both":
        return "web_agent"
    return "response_agent"

builder.add_conditional_edges("rag_agent", route_after_rag, {
    "web_agent": "web_agent",
    "response_agent": "response_agent",
})

# Web Agent → Response Agent
builder.add_edge("web_agent", "response_agent")

# Response Agent → Save Node
builder.add_edge("response_agent", "save_node")

# Save Node → END
builder.add_edge("save_node", END)

# Compile the graph
graph = builder.compile()