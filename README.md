# Finance RAG

A Retrieval-Augmented Generation (RAG) application for querying financial documents. This project allows users to upload PDF, Excel, or CSV files containing financial data, process them into chunks, embed them, and perform question-answering using a vector store and an Ollama model.

## Features

- **Document Upload**: Support for PDF, Excel (.xlsx, .xls), and CSV files.
- **Text Processing**: Splits documents into manageable chunks.
- **Embeddings**: Generates embeddings for chunks using an embedder.
- **Vector Search**: Stores embeddings in a vector store for efficient retrieval.
- **Q&A Interface**: Interactive chat interface powered by Streamlit to ask questions and get answers based on the uploaded documents.
- **Model Integration**: Uses Ollama models (e.g., gemma3:1b) for generating responses.

## Installation

1. Clone the repository or navigate to the project directory.

2. Install the required dependencies:
   ```
   pip install -r requirement.txt 
   ```
   And
   ```
   pip install ollama
   ```
   
   Note: Ensure you have Ollama installed and running locally. You may need additional libraries like `langchain`, `faiss`, or others depending on the embedder and vector store implementations.

4. If not already present, create a `requirements.txt` file with the necessary packages.

## Usage

1. Start the Streamlit app:
   ```
   streamlit run app.py
   ```

2. In the sidebar:
   - Upload one or more financial documents (PDF, Excel, CSV).
   - Specify the Ollama model name (default: gemma3:1b).
   - Click "Process documents" to embed and store the content.

3. In the main chat area:
   - Ask questions related to the uploaded documents, e.g., "What was the net income?"
   - The app will retrieve relevant chunks and generate an answer using the specified model.

## Project Structure

- `app.py`: Main Streamlit application.
- `loaders.py`: Functions to load and extract text from PDF, Excel, and CSV files.
- `splitter.py`: Text splitting logic.
- `embedder.py`: Embedding generation for text chunks.
- `vector_store.py`: Vector store implementation for similarity search.
- `qa.py`: Question-answering logic using the model.
- `test.py`: Test scripts.
- `samples/`: Sample data files (e.g., sample_financial_statement.xlsx).

## Requirements

- Python 3.8+
- Streamlit
- Ollama (with a compatible model like gemma3:1b)
- Other dependencies as per your embedder/vector store (e.g., sentence-transformers, faiss-cpu)

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is licensed under the MIT License.

---

© 2024 Swapnil Mishra
