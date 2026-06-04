from langchain_community.tools import DuckDuckGoSearchResults

def web_tool(question):
    search_tool = DuckDuckGoSearchResults()
    response = search_tool.invoke(question)
    return response


def save_tool(question, response, resource):
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
            "\n" + "="*50 + "\n"
        )
    