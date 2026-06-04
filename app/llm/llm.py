from langchain_ollama import ChatOllama

from app.config.config import Config

llm = ChatOllama(model = Config.model)

