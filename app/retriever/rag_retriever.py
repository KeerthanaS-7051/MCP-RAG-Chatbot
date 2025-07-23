from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings 
from langchain.text_splitter import CharacterTextSplitter
from app.retriever.schema_loader import extract_schema_and_rows

db_path = "employee.db"

# Load schema and sample data
docs = extract_schema_and_rows(db_path)
text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
split_docs = text_splitter.create_documents(docs)

# Vectorstore
embedding = OpenAIEmbeddings()  
vectorstore = FAISS.from_documents(split_docs, embedding)

def retrieve_context(query: str, k: int = 4) -> str:
    relevant_docs = vectorstore.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in relevant_docs])
