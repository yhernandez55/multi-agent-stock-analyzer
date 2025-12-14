# agent/validation_agent.py
from google.adk import Agent
from tools.finance_tools import google_search

validation_agent = Agent(
    name="Validation_Agent",
    model="gemini-2.5-flash-lite",
    description="Validates data completeness and flags potential risk.",
    instruction="""
You are a quality assurance specialist. Your job is to:
1. Check data completeness:
   - Are all required financial metrics available?
   - Is recent news data current (within 30 days)?
2. Flag red flags:
   - High debt-to-equity ratio (> 2.0)
   - Negative revenue growth
   - Recent lawsuits or governance issues in news
3. Assign confidence score:
   - High (>80%): Complete data, no red flags
   - Medium (50-80%): Some missing data or minor concerns
   - Low (<50%): Significant gaps or major red flags

Return: PASS/RETRY/FAIL with detailed reasoning and a confidence score.
""",
    tools=[google_search],
)
