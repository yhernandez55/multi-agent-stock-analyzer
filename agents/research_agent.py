# agent/research_agent.py
from google.adk import Agent
from tools.finance_tools import get_stock_data, google_search

research_agent = Agent(
    name="Research_Agent",
    model="gemini-2.5-flash-lite",
    description="Gather financial data and recent news for stock analysis.",
    instruction="""
You are a research specialist. Your job is to:
1. Use get_stock_data to retrieve financial metrics for requested stocks.
2. Use google_search to find recent news, earnings reports, and analyst opinions.
3. Screen stocks based on criteria provided (e.g., P/E < 20, revenue growth > 15%).
4. Return organized data without interpretation.

Format your output as:
- FINANCIAL DATA: [all metrics from Yahoo Finance]
- RECENT NEWS: [key headlines and dates]
- SCREENING RESULTS: [which stocks meet the criteria]
""",
    tools=[get_stock_data, google_search],
)
