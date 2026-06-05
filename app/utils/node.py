from app.utils.tools import save_tool
from app.utils.state import State


def save_node(state: State) -> dict:
    """Save the conversation to chat_history.txt."""
    save_tool(state["question"], state["response"], state["resource"])
    return {
        "response": state["response"],
        "resource": state["resource"],
    }