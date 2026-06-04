from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from app.llm.llm import llm
from app.config.config import Config
from app.prompts.prompt import prompt

embeddings = OllamaEmbeddings(model=Config.embedding_model)

vector_store = FAISS.load_local(
    'save_index',
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.6}  
)

chain = prompt | llm