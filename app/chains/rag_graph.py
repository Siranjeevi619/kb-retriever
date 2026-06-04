from app.utils.node import web_node, rag_node, retreiver, route, save_node
from langgraph.graph import StateGraph
from langgraph.graph import START, END
from app.utils.state import State

builder = StateGraph(State)

builder.add_node("rag_node", rag_node)
builder.add_node("retriever", retreiver)
builder.add_node("web_node", web_node)
builder.add_node("save_node", save_node)


builder.add_edge(START, "retriever")


builder.add_conditional_edges("retriever", route, {
    "rag":"rag_node",
    "web":"web_node"
})

builder.add_edge("web_node", "save_node")
builder.add_edge("rag_node", "save_node")

builder.add_edge("save_node", END)

graph = builder.compile()