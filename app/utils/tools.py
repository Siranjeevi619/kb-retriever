from langchain_community.tools import DuckDuckGoSearchResults

def web_tool(question):
    search_tool = DuckDuckGoSearchResults()
    response = search_tool.invoke(question)
    return response