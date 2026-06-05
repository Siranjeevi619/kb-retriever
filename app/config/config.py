from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    model=os.getenv("MODEL")
    embedding_model = os.getenv("EMBEDDING_MODEL")
    groq_api = os.getenv("GROQ_API")
    