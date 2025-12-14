# agent/coordinating_agent.py
from google.adk import Agent
from tools.finance_tools import get_stock_data, google_search
from tools.memory import (
    conversation_history,
    user_profile,
    update_memory,
    get_memory_context
)

coordinating_agent = Agent(
    name="Investment_Research_Agent",
    model="gemini-2.5-flash-lite",
    description="Provides investment research and stock recommendations with chain-of-thought reasoning.",
    instruction="""
You are an investment research assistant. When analyzing stocks:

1. RESEARCH: Use get_stock_data and google_search to gather information.
2. ANALYZE: For each stock, run a 3-step analysis:
   - VALUATION: Compare P/E to sector average (~25 for tech) and 52-week range.
   - GROWTH: Review revenue growth and profit margins.
   - RISK: Check debt-to-equity and recent negative news.
3. RECOMMENDATION: Synthesize above to give BUY/HOLD/AVOID + Confidence (High/Medium/Low).

Format output like:
=== [TICKER]: [COMPANY NAME] ===
🔍 ANALYSIS:
• Valuation: ...
• Growth: ...
• Risk: ...
📊 RECOMMENDATION: [BUY/HOLD/AVOID] — Confidence: [High/Medium/Low]
Key Metrics:
- Current Price: $X
- P/E Ratio: X
- Revenue Growth: X%
- Debt-to-Equity: X
Always show short reasoning and cite specific metrics.
""",
    tools=[get_stock_data, google_search],
)
