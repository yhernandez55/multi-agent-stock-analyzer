# tools/memory.py
from datetime import datetime

# Short-term: Store conversation context
conversation_history = []

# Long-term: Track user preferences
user_profile = {
    "risk_tolerance": "moderate",
    "preferred_sectors": [],
    "preferred_market_cap": "any",
    "dividend_preference": False,
    "max_pe_ratio": None,
    "min_revenue_growth": None,
    "excluded_companies": [],
    "past_recommendations": [],
    "past_queries": [],
}

# updating the memory
def update_memory(user_query: str, agent_response: str, stocks_mentioned: list):
    """Updates both short-term and long-term memory"""
    conversation_history.append({
        "timestamp": datetime.utcnow().isoformat(),
        "query": user_query,
        "response": agent_response,
        "stocks": stocks_mentioned
    })

    user_profile["past_queries"].append(user_query)
    user_profile["past_recommendations"].extend(stocks_mentioned)

def get_memory_context() -> str:
    """Formats memory into a context string for the agent"""
    recent = conversation_history[-3:]
    if not recent:
        return ""

    context = "User context from previous interactions:\n"
    for r in recent:
        context += f"- Asked: {r['query']} | Mentioned stocks: {r['stocks']}\n"

    return context