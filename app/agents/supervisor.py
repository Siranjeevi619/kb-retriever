from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate
from app.utils.state import State


SUPERVISOR_PROMPT = ChatPromptTemplate.from_template(
    """You are a supervisor agent that routes user questions to the right specialist.

You have two specialist agents available:
1. **RAG Agent** — Has access to a local knowledge base (PDF documents about machine learning). 
   Use this for questions that are likely covered in the stored documents.
2. **Web Search Agent** — Can search the internet for current or general information.
   Use this for questions about recent events, general knowledge, or topics not in the knowledge base.

Analyze the user's question and decide which agent(s) should handle it.

Rules:
- If the question is about machine learning concepts, algorithms, or topics likely in the knowledge base, respond with: rag
- If the question is about current events, general knowledge, or something unlikely to be in the knowledge base, respond with: web
- If the question could benefit from both sources, respond with: both
- You MUST respond with EXACTLY one of these three words: rag, web, both

User's question: {question}

Your routing decision:"""
)


def supervisor_node(state: State) -> dict:
    """Supervisor agent that analyzes the question and decides routing."""
    chain = SUPERVISOR_PROMPT | llm
    response = chain.invoke({"question": state["question"]})
    
    # Parse the decision — extract just the routing keyword
    decision = response.content.strip().lower()
    
    # Ensure we get a valid routing decision
    if "both" in decision:
        next_agent = "both"
    elif "web" in decision:
        next_agent = "web"
    else:
        next_agent = "rag"
    
    return {"next_agent": next_agent}
