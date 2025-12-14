# runner/run_local_demo.py
import asyncio
import logging
import os
from dotenv import load_dotenv  
from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import LoggingPlugin
from tools.memory import (
    conversation_history,
    user_profile,
    update_memory,
    get_memory_context
)
from agents.coordinating_agent import coordinating_agent

# Loading environment variabbles from .env file
load_dotenv()

# ✅ Verify API key
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError(
        "❌ GOOGLE_API_KEY not found!\n"
        "Copy .env.example to .env and add your Gemini API key."
    )


logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

async def main():
    runner = InMemoryRunner(
        agent=coordinating_agent, 
        plugins=[LoggingPlugin()]
    )
    
    demo_queries = [
        "Find undervalued tech stocks with P/E under 20",
        "Should I invest in Apple right now?",
        "Compare Microsoft vs Google as investments"
    ]
    
    print("🚀 Running Investment Agent Demo\n")
    
    for query in demo_queries:
        print("="*70)
        print(f"Query: {query}")
        print("="*70)
        
        events = await runner.run_debug(query)
        
        # Extract response text
        response_text = ""
        for event in events:
            if hasattr(event, "content") and hasattr(event.content, "parts"):
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text:
                        response_text += part.text
        
        print(response_text)
        print("\n")

if __name__ == "__main__":
    asyncio.run(main())