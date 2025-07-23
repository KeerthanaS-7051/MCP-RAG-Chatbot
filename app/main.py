from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from app.context_store import context_store

app = FastAPI()

class ContextRequest(BaseModel):
    session_id: str
    context: Dict[str, Any]

@app.get("/context/{session_id}")
def get_context(session_id: str):
    return context_store.get_context(session_id)

@app.post("/context")
def update_context(data: ContextRequest):
    context_store.update_context(data.session_id, data.context)
    return {"status": "updated"}
