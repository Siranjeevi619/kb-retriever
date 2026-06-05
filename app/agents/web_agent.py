from langgraph.prebuilt import create_react_agent
from app.llm.llm import llm
from app.utils.tools import web_search
from app.utils.state import State


WEB_SYSTEM_PROMPT = (
    "You are a Web Search specialist agent. "
    "Your job is to answer the user's question by searching the internet for relevant information. "
    "Use the web_search tool to find current and accurate information, then provide a clear and "
    "comprehensive answer based on the search results. Cite your sources when possible. "
    "You MUST use the web_search tool — do NOT attempt to answer from your own knowledge."
)

# Create the Web Search react agent with the web_search tool
web_react_agent = create_react_agent(
    model=llm.bind_tools([web_search]),
    tools=[web_search],
    prompt=WEB_SYSTEM_PROMPT,
)


def web_agent_node(state: State) -> dict:
    """Web Search agent node — invokes the react agent and returns the response."""
    try:
        result = web_react_agent.invoke(
            {"messages": [("user", state["question"])]}
        )
        # Extract the final AI message content
        final_message = result["messages"][-1].content
    except Exception as e:
        # Fallback: call the tool directly if the agent fails
        from app.utils.tools import web_search as ws
        raw_result = ws.invoke(state["question"])
        final_message = f"Web search results:\n{raw_result}"

    return {
        "web_response": final_message,
    }
