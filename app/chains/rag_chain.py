from langchain_community.vectorstores import FAISS
from app.llm.llm import llm
from app.embeddings.embedding import embeddings
from app.prompts.prompt import prompt


vector_store = FAISS.load_local('save_index', embeddings=embeddings, allow_dangerous_deserialization=True)

retriever = vector_store.as_retriever(search_kwargs = {"k":3})

chain = prompt | llm