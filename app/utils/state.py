from typing import TypedDict, List
from langchain_core.documents import Document

class State(TypedDict):
    question: str
    document: List[Document]
    response: str
    resource: str