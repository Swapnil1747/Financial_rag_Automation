import streamlit as st
from loaders import load_pdf, load_excel, load_csv
from splitter import split_text
from embedder import embed_chunks, embed_text
from vector_store import VectorStore
from qa import answer_query

st.set_page_config(page_title="RAG Financial Assistant", layout="wide")
st.title("📊 Financial Document Q&A (RAG)")
with st.expander("ℹ️ About this App", expanded=False):
    st.markdown("""
    ### 💼 Financial Document Q&A Assistant — UI Overview

    **🧭 Layout Structure**  
    The application is organized into a clean, responsive two-column layout:
    - **Left Sidebar**: Document ingestion and model configuration  
    - **Main Panel**: Interactive assistant chat, extracted metrics, and table previews

    **📁 Sidebar: Document Upload & Configuration**  
    - Upload PDFs, Excel (.xls, .xlsx), or CSV files (max 200MB each)  
    - Select your local Ollama model By input(e.g., `gemma3:1b`, `llama3:8b`)  
    - Click “Process documents” to parse, chunk, embed, and index your data

    **💬 Main Panel: Assistant Interaction**  
    - Ask natural language questions like “What was net income in FY 2022?”  
    - The assistant responds strictly based on your uploaded data — no hallucinations  
    - Chat history is preserved for multi-turn conversations

    **📊 Extracted Metrics Section**  
    - Displays key financial metrics like `net_income = -2.97B`, `cash_and_equivalents = 5.11B`  
    - Metrics are shown in a compact, readable format for quick reference

    **📋 Table Preview Section**  
    - Shows up to four extracted tables from your documents  
    - All rows and columns are preserved, including missing values (`NaN`)  
    - Ensures full transparency and traceability of financial data

    **🛡️ Data Integrity & Grounding**  
    - Answers are strictly retrieval-augmented from your uploaded files  
    - If a question cannot be answered, the assistant says “No data available for your question”  
    - This ensures trustworthiness and auditability for financial analysis
    """)
st.markdown("**Author:** Swapnil Mishra —> Financial Automation Developer")    


if "store" not in st.session_state:
    st.session_state.store = None
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    uploaded_files = st.file_uploader("Upload PDF, Excel, or CSV", type=["pdf", "xlsx", "xls", "csv"], accept_multiple_files=True)
    model_name = st.text_input("Ollama model", value="gemma3:1b")
    process_btn = st.button("Process documents")

def process(files):
    all_text = []
    for f in files:
        data = f.read()
        if f.name.endswith(".pdf"):
            all_text.append(load_pdf(data))
        elif f.name.endswith((".xlsx", ".xls")):
            all_text.append(load_excel(data))
        elif f.name.endswith(".csv"):
            all_text.append(load_csv(data))
    full_text = "\n\n".join(all_text)
    chunks = split_text(full_text)
    embeddings = embed_chunks(chunks)
    store = VectorStore(embeddings, chunks)
    return store, chunks

if process_btn and uploaded_files:
    with st.spinner("Processing..."):
        store, chunks = process(uploaded_files)
        st.session_state.store = store
        st.session_state.chunks = chunks
        st.session_state.messages = []
    st.success(f"✅ Processed {len(uploaded_files)} file(s) into {len(chunks)} chunks.")

st.subheader("💬 Ask a question")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask something like: What was net income?")
if query:
    if not st.session_state.store:
        st.warning("Please upload and process documents first.")
    else:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                q_embed = embed_text(query)
                retrieved = st.session_state.store.search(q_embed, k=5)
                answer = answer_query(model_name, query, retrieved)
                st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
