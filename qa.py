from ollama_client import generate_ollama

SYSTEM_PROMPT = """You are a financial assistant.
Only answer using the provided context.
If the answer is not clearly present, say 'No data available for your question.'
Do not guess or use external knowledge."""

def build_prompt(query: str, chunks: list[str]) -> str:
    context = "\n".join([f"-- Chunk {i+1} --\n{ch}" for i, ch in enumerate(chunks)])
    return f"[User Question]\n{query}\n\n[Context]\n{context}"

def answer_query(model: str, query: str, retrieved_chunks: list[str]) -> str:
    prompt = build_prompt(query, retrieved_chunks)
    return generate_ollama(model, prompt, system=SYSTEM_PROMPT, temperature=0.1)
