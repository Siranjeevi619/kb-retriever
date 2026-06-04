from langchain_community.vectorstores import FAISS
from app.embeddings.embedding import embeddings
from app.embeddings.ingest import chunks

vectorDB = FAISS.from_documents(documents=chunks, embedding=embeddings )

vectorDB.save_local('save_index')