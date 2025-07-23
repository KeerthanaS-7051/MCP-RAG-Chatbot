import sqlite3
from langchain_core.documents import Document

def load_database_docs(db_path: str = "employee.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='employee';")
    schema = cursor.fetchone()[0]
    schema_doc = Document(page_content=schema, metadata={"source": "schema"})

    cursor.execute("SELECT * FROM employee;")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    row_docs = []
    for row in rows:
        text = ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
        row_docs.append(Document(page_content=text, metadata={"source": "row"}))

    conn.close()
    return [schema_doc] + row_docs
