from langchain_community.llms import Together
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
import sqlite3
import time

llm = Together(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    temperature=0.3,
    max_tokens=512,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_retriever(db_path: str = "employee.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table'")
    schema_info = "\n".join(row[0] for row in cursor.fetchall())

    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    rows_text = "\n".join(str(dict(zip(col_names, row))) for row in rows)

    conn.close()

    full_text = f"Schema:\n{schema_info}\n\nData:\n{rows_text}"

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [Document(page_content=chunk) for chunk in text_splitter.split_text(full_text)]

    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore.as_retriever()

retriever = get_retriever()

def generate_sql(question: str) -> str:
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
You are an expert SQL assistant. Your task is to convert a user's question into a valid and syntactically correct **SQLite query**.

Follow these rules:
- Assume the table name is `employee` unless the user specifies otherwise.
- Use standard SQLite syntax only.
- Return **only** the SQL query, no explanations or extra text.

User question: {question}
SQL query:
"""
    )
    result = llm.invoke(prompt.format(question=question)).strip()
    time.sleep(2.5)  
    return result

def generate_response(question: str, sql_result: str) -> str:
    prompt = PromptTemplate(
        input_variables=["question", "sql_result"],
        template="""
You are a helpful assistant. The user asked a question, and you've already executed the SQL query to get the result.

Now, based on the SQL result below, provide a clear and concise natural language answer to the original question.

User question: {question}
SQL result: {sql_result}

Answer:
"""
    )
    result = llm.invoke(prompt.format(question=question, sql_result=sql_result)).strip()
    time.sleep(2.5) 
    return result

def answer_with_rag(question: str) -> str:
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return qa.run(question)
