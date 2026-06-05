from typing import TypedDict, List, Optional
from langchain_core.documents import Document


class State(TypedDict):
    question: str
    document: List[Document]
    rag_response: str          # Output from RAG agent
    web_response: str          # Output from Web Search agent
    response: str              # Final synthesized response
    resource: str              # Source attribution (RAG, web, both)
    next_agent: str            # Supervisor routing decision: "rag", "web", or "both"