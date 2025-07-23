from app.llm import generate_sql, generate_response
from app.tools.sql_tool import run_sql_query
from app.context_store import context_store

def chat(session_id: str, user_query: str):
    try:
        sql = generate_sql(user_query)
        result = run_sql_query(sql)
        final_answer = generate_response(user_query, result)

        context_store.update_context(session_id, {
            "conversation_history": [("user", user_query), ("assistant", final_answer)]
        })

        return {"response": final_answer}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}
