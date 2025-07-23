class ContextStore:
    def __init__(self):
        self.data = {}

    def get_context(self, session_id):
        return self.data.setdefault(session_id, {
            "system_prompt": "You are a helpful assistant.",
            "conversation_history": [],
            "memory": {},
            "tools": ["sql_tool"]
        })

    def update_context(self, session_id, context):
        session = self.get_context(session_id)
        for k, v in context.items():
            if k == "conversation_history":
                session["conversation_history"].extend(v)
            else:
                session[k] = v

context_store = ContextStore()
