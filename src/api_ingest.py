import requests
import os
from src.config import ALPHA_VANTAGE_API_KEY

def fetch_company_data(symbol="ADBE"):
    """
    Fetches real-time market data. 
    If API fails, returns None to allow seamless fallback to internal reports.
    """
    try:
        # Use the key from config
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
        
        response = requests.get(url, timeout=5)
        data = response.json()

        # 'Error Message' on wrong keys
        if "Name" not in data:
            print(f"API Info: {data.get('Note', data.get('Error Message', 'Unknown API Error'))}")
            return None

        # Standardizing the output for the RAG engine
        docs = [
            {"text": f"Company {data.get('Name')} Overview: {data.get('Description')}", "source": "Alpha_Vantage_API"},
            {"text": f"Financials: Market Cap {data.get('MarketCapitalization')}, Revenue TTM {data.get('RevenueTTM')}", "source": "Alpha_Vantage_API"},
            {"text": f"Risk Profile: Beta is {data.get('Beta')}, 52-Week High {data.get('52WeekHigh')}", "source": "Alpha_Vantage_API"}
        ]
        
        print(f"Successfully integrated data for {symbol} via Alpha Vantage")
        return docs

    except Exception as e:
        print(f"Connection error: {e}")
        return None