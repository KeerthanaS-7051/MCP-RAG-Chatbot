import sqlite3

def extract_schema_and_rows(db_path: str, max_rows: int = 5):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    documents = []
    
    for table in tables:
        # Schema
        cursor.execute(f"PRAGMA table_info({table});")
        schema_info = cursor.fetchall()
        schema_text = f"Table `{table}` has columns: " + ", ".join(
            f"{col[1]} ({col[2]})" for col in schema_info
        )
        documents.append(schema_text)

        # Sample Rows
        cursor.execute(f"SELECT * FROM {table} LIMIT {max_rows};")
        rows = cursor.fetchall()
        for row in rows:
            row_text = f"Row in `{table}`: " + ", ".join(str(item) for item in row)
            documents.append(row_text)
    
    conn.close()
    return documents
