# 🧠 ResearchQA: Research Paper Question-Answering System (RAG + Ollama)

This project is a **Research Paper Question-Answering System** built with the Retrieval-Augmented Generation (RAG) approach using **LangChain**, **Ollama** (for local LLMs), **ChromaDB**, and **Streamlit**. It enables researchers to **ask natural language questions** over uploaded research papers (PDF format), and get concise answers powered by a local LLM like `mistral`.

---

## 🚀 Features

- 📄 Upload and process research papers in PDF format
- 🔍 Uses semantic search via `ChromaDB` vector store
- 🧠 Integrates with `mistral` LLM running locally via **Ollama**
- 🦜 Built using LangChain's RAG pipeline
- 💬 Intuitive UI built with Streamlit

---

## 🖼️ Architecture

[PDF Research Paper] → [LangChain PDF Loader]
↓
[Text Splitting]
↓
[Embeddings via SentenceTransformer]
↓
[ChromaDB Vector Store (FAISS-like)]
↓
[User Question] → [LangChain RetrievalQA Chain] → [Ollama LLM (mistral)] → [Answer]


---

## 🛠️ Installation

1. Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate      # On Windows

2. Install Dependencies
3. 
pip install -r requirements.txt

5. Install and Run Ollama
Install Ollama (if not installed):

🔗 https://ollama.com/download

Start Ollama and pull the mistral model:
ollama pull mistral
ollama run mistral
🧪 Running the App

streamlit run app.py
Upload your research paper (PDF), ask a question, and get contextual answers!


🧠 Models Used
Sentence Transformers: all-MiniLM-L6-v2 for generating embeddings

LLM: mistral via Ollama

🧩 External Tools Used
LangChain

Ollama – Local LLMs like mistral

ChromaDB – Lightweight vector store

Streamlit – Interactive UI

📌 Notes
Ensure ollama server is running before starting the app.

Make sure the mistral model is pulled (ollama pull mistral).
