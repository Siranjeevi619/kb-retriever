from langchain_groq import ChatGroq

from app.config.config import Config

llm = ChatGroq(model = Config.model , groq_api_key = Config.groq_api)

