# AI-Leadership-Insight-Decision-Agent
This project was designed to create an AI Leadership Insight and Decision Assistant that is capable of combining internal corporate documents with real-time market data to provide answers to business strategy questions. This was accomplished by utilizing a combination of a Retrieval Augmented Generation (RAG) pipeline and live APIs.

Quick Start:
1. Install Dependencies: `pip install -r requirements.txt`
2. Configure API: Add your key to `src/config.py`.
3. Run Agent: `python main.py`


System Architecture:
The agent uses a "Dual-Stream" intelligence model:
1) Internal Stream: Processes unstructured company reports (Annual/Quarterly/Operational) using FAISS and Sentence Transformers.
2) External Stream: Fetches live market metrics via the Alpha Vantage API.

[Internal Docs] + [Live API Data] → Semantic Search → Adaptive LLM Synthesis → Executive Report
Initially, it was a static fallback response, but I made it dynamic by generating insights from the context using it.

### 📁 Project Structure

```text
ai-agent/
├── data/                      # Internal Ground Truth
│   ├── annual_report.txt
│   ├── quarterly_report.txt
│   └── operational_updates.txt
├── src/                       # Core Logic
│   ├── config.py              # API Key Configuration
│   ├── ingest.py              # Document Chunking
│   ├── api_ingest.py          # Alpha Vantage Integration
│   ├── retrieval.py           # FAISS & Semantic Search
│   ├── llm.py                 # Intent-Based Generation
│   └── visualization.py       # Financial Plotting
├── evaluation/                # Testing
│   ├── eval.py
│   └── test_questions.json
├── outputs/                   # Generated Plots
├── main.py                    # Entry Point
├── requirements.txt
└── README.md
```

Setup & Verification:
1. Install Dependencies
Bash
pip install -r requirements.txt
2. Configure API Key
To enable Autonomous Research, obtain a free key from Alpha Vantage and add it to src/config.py:
ALPHA_VANTAGE_API_KEY = "YOUR_KEY_HERE"
3. Run the Agent
Bash
python main.py
Verification: The "Adobe" (ADBE) Test
To verify the system's ability to handle dynamic, real-world requests:
Run main.py.


The agent will fetch Adobe’s live market cap and volatility, merging it with the internal strategic context found in the /data folder.

Adaptive Output Examples
Input: "What is the budget?" Output: Generates an ADAPTIVE BUDGETARY ANALYSIS focusing on fiscal allocations and department misses.
Input: "What are our risks?" Output: Generates an ADAPTIVE RISK REPORT highlighting internal attrition (22%) and external market volatility.

Visualization:
The system automatically generates a revenue trend graph in the outputs folder when revenue-related queries are asked.
Source: Merges internal $4.2B historical data with live API revenue metrics.
Format: Saved as outputs/revenue_plot.png.

Key Features:
1) Hybrid Intelligence: Merges local .txt files with live Cloud API data.
2) Intent Detection: Automatically switches report formats based on user query (Financial vs. Risk vs. Performance).
3) Grounded Citations: Every insight includes source tagging (e.g., [annual_report.txt] or [Alpha_Vantage_API]).
4) Failsafe Design: Seamlessly falls back to internal documents if API limits are reached.
5) Automated Visuals: Generates PNG charts for any revenue-related inquiry.

Assumptions:
Documents are provided as unstructured text files in /data.
The system uses the all-MiniLM-L6-v2 model for local CPU-efficient embedding.
Alpha Vantage free-tier API is subject to rate limits (5 requests/min).

Conclusion:
This agent demonstrates how AI can bridge the gap between static internal knowledge and the rapidly changing external market, providing leaders with a 360-degree view of their organization's health.

Author: Arya Brijith
