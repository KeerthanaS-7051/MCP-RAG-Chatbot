#  MCP RAG Chatbot

A lightweight, modular chatbot that answers questions using **RAG (Retrieval-Augmented Generation)** on an **SQLite-based employee database**. It uses **LangChain**, **Together AI's LLaMA 3 model**, and **Streamlit** for the UI.

---

##  Features

-  Converts natural language questions into SQL
-  Retrieves results from SQLite database
-  Generates human-friendly answers
-  Uses RAG with schema + row indexing
-  Pretty chat history with memory
-  Local vectorstore using FAISS
-  UI via Streamlit

---


---

##  Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/mcp-rag-chatbot.git
cd mcp-rag-chatbot
```

### 2. Create Virtual Environment and Install Dependancies

```bash
python -m venv venv
venv\Scripts\activate   
pip install -r requirements.txt
```
### 3. Set Environment Variable

```bash
export TOGETHER_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
streamlit run streamlit_app.py
```
