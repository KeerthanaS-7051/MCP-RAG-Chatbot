import sqlite3

def run_sql_query(query: str, db_path: str = "employee.db") -> str:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [description[0] for description in cursor.description]
        conn.close()

        if not rows:
            return "No matching records found."

        result = [dict(zip(col_names, row)) for row in rows]
        return str(result)

    except Exception as e:
        return f"Error running SQL: {str(e)}"
