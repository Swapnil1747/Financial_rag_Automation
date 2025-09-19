import faiss
import numpy as np

class VectorStore:
    def __init__(self, embeddings: list[list[float]], chunks: list[str]):
        self.chunks = chunks
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings))

    def search(self, query_embedding: list[float], k=5) -> list[str]:
        D, I = self.index.search(np.array([query_embedding]), k)
        return [self.chunks[i] for i in I[0]]
