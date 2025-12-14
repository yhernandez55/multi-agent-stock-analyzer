# tools/finance_tools.py
import os
try:
    import yfinance as yf
except Exception:
    yf = None

# Optional: load GOOGLE_API_KEY from env (works locally or in Kaggle if set)
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

def get_stock_data(ticker: str) -> dict:
    """
    Retrieves basic financial data for a given ticker using yfinance.
    This is intentionally defensive - returns readable placeholders if yfinance not available.
    """
    if yf is None:
        return {"ticker": ticker, "error": "yfinance not installed in this environment."}

    try:
        stock = yf.Ticker(ticker)
        info = stock.info or {}
        return {
            "ticker": ticker,
            "company_name": info.get("longName", "N/A"),
            "current_price": info.get("currentPrice", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "revenue_growth": info.get("revenueGrowth", "N/A"),
            "profit_margin": info.get("profitMargins", "N/A"),
            "debt_to_equity": info.get("debtToEquity", "N/A"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
        }
    except Exception as e:
        return {"ticker": ticker, "error": f"Failed to retrieve data: {e}"}

def google_search(query: str) -> str:
    """
    Placeholder search tool. Replace with real search integration if available.
    Returns a short human-readable string summarizing "search results".
    """
    # For privacy/simplicity we default to a placeholder. Replace here with web requests if you wire up an API.
    return f"Placeholder search results for query: {query} (no live search configured)."
