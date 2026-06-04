from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
path = './app/source/random machine learing pdf.pdf'


loader = PyPDFLoader(path)

document = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

chunks = splitter.split_documents(document)
