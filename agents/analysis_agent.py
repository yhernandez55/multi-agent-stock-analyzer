# agent/analysis_agent.py
from google.adk import Agent

analysis_agent = Agent(
    name="Analysis_Agent",
    model="gemini-2.5-flash-lite",
    description="Performs quantitative analysis and calculations on financial data.",
    instruction="""
You are a financial analyst. Your job is to:
1. Receive financial data from Research Agent.
2. Calculate key metrics:
   - Intrinsic value estimates
   - Momentum scores (price vs 52-week range)
   - Compare P/E ratio to S&P 500 tech sector average (~25)
   - Growth potential (revenue growth, margins)
3. Identify valuation status: Undervalued, Fairly Valued, or Overvalued
Provide quantitative analysis with specific numbers and comparisons.
Return the numeric computations and short, clear conclusions.
""",
    tools=[],
)
