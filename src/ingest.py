import os

def load_documents(folder="data"):
    docs = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r") as f:
            docs.append({"text": f.read(), "source": file})
    return docs

def chunk_text(text, size=300):
    return [text[i:i+size] for i in range(0, len(text), size)]

def process_documents(docs):
    chunks = []
    for doc in docs:
        text_chunks = chunk_text(doc["text"])
        for chunk in text_chunks:
            chunks.append({
                "content": chunk,
                "source": doc["source"]
            })
    return chunks


