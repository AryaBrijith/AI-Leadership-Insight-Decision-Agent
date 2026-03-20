import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    return model.encode(texts)

def build_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def retrieve(query, chunks, index, k=3):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results