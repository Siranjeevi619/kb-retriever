from langchain_ollama import OllamaEmbeddings
from app.config.config import Config
embeddings = OllamaEmbeddings(model=Config.embedding_model )

