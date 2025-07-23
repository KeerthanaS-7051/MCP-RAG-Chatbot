import streamlit as st
from chatbot import chat
import uuid

st.set_page_config(page_title="MCP RAG Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

st.title("🤖 MCP RAG Chatbot")
st.write("Ask a question related to the employee database:")

user_input = st.text_input("Your question", key="input")

if user_input:
    result = chat(st.session_state.session_id, user_input)
    st.markdown(f"**SQL Query:** `{result.get('sql')}`")
    st.markdown(f"**Response:** {result.get('response')}")

    st.markdown("---")
    st.subheader("Chat History")
    history = st.session_state.get("history", [])
    history.append((user_input, result.get("response")))
    st.session_state.history = history

    for i, (q, a) in enumerate(reversed(history), 1):
        st.markdown(f"**{i}. You:** {q}")
        st.markdown(f"**Bot:** {a}")
