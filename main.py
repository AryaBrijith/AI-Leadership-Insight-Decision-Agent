import os
from src.config import ALPHA_VANTAGE_API_KEY
from src.api_ingest import fetch_company_data
from src.ingest import load_documents, process_documents
from src.retrieval import embed_texts, build_index, retrieve
from src.llm import generate_answer
from src.visualization import plot_revenue

def start_agent():
    print("---AI Leadership Insight & Decision Agent Initialized ---")
    
    # Using internal docs-contains the ground truth
    print("Ingesting internal company documents...")
    raw_internal_docs = load_documents("data")
    internal_chunks = process_documents(raw_internal_docs)
    embeddings = embed_texts([c["content"] for c in internal_chunks])
    index = build_index(embeddings)
    while True:
        query = input("\nAsk Leadership Question (or type 'exit'): ")
        if query.lower() == 'exit': break

        knowledge_stack = []
        
        # Using External API First
        print("Checking External API for real-time data...")
        api_data = fetch_company_data()
        
        if api_data:
            knowledge_stack.extend([{"content": d["text"], "source": d["source"]} for d in api_data])
        
        print("Retrieving facts from internal knowledge base...")
        
        report_results = retrieve(query, internal_chunks, index, k=3)
        knowledge_stack.extend(report_results)

        print("Synthesizing final report...")
        answer = generate_answer(query, knowledge_stack)
        
        print("\n" + "="*30)
        print(answer)
        print("="*30)

        if "revenue" in query.lower() or "trend" in query.lower():
            plot_revenue()
            print("Graph generated in outputs/revenue_plot.png")

if __name__ == "__main__":
    start_agent()