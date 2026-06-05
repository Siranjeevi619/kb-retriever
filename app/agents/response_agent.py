from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate
from app.utils.state import State


RESPONSE_PROMPT = ChatPromptTemplate.from_template(
    """You are a response synthesis agent. Your job is to create a final, coherent response 
for the user based on the outputs from specialist agents.

User's original question: {question}

{agent_outputs}

Instructions:
- Synthesize the information into a clear, well-structured response.
- If both RAG and Web sources provided answers, combine the insights and note which information came from which source.
- If only one source provided an answer, present that answer clearly.
- Be concise but thorough.

Your synthesized response:"""
)


def response_agent_node(state: State) -> dict:
    """Response agent — synthesizes outputs from specialist agents into a final answer."""
    
    # Build the agent outputs section based on what's available
    agent_outputs = []
    sources = []
    
    rag_response = state.get("rag_response", "")
    web_response = state.get("web_response", "")
    
    if rag_response:
        agent_outputs.append(f"**RAG Agent (Knowledge Base) Response:**\n{rag_response}")
        sources.append("RAG")
    
    if web_response:
        agent_outputs.append(f"**Web Search Agent Response:**\n{web_response}")
        sources.append("web-search")
    
    agent_outputs_text = "\n\n".join(agent_outputs) if agent_outputs else "No agent provided a response."
    
    # Determine resource attribution
    resource = " + ".join(sources) if sources else "none"
    
    chain = RESPONSE_PROMPT | llm
    response = chain.invoke({
        "question": state["question"],
        "agent_outputs": agent_outputs_text,
    })
    
    return {
        "response": response.content,
        "resource": resource,
    }
