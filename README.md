# 🤖 AI Investment Research Agent

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4)](https://github.com/google/adk)

> **Capstone Project**: 5-Day AI Agents Intensive Course with Google  
> **Track**: AI Financial Assistant
> **Author**: Yanelly Hernandez
> **Submission Date**: December 1, 2025
**Added local version Date**: December 13, 2025

An intelligent agent that automates stock investment research, reducing analysis time from 2+ hours to 3 minutes while maintaining 85% quality assurance standards.

---

## 🎯 Quick Links

- 📓 [**Live Kaggle Demo**](notebooks/ai-financial-assistant.ipynb)
- 🎥 [**Screenshot Example**](https://github.com/user-attachments/assets/3b77fb72-b25d-4833-beca-4f7aa5793410)
- 💻 [**Local Setup**](demos/run_local_demo.py) - Run on your machine

---


## 📊 Project Overview

### The Problem

Individual investors face significant challenges when researching stocks:

**Impact**: Investors analyze fewer opportunities, miss potential gains, and make emotion-driven decisions.

### The Solution

An AI-powered investment research agent that:

1. **Automates Data Collection**: Real-time financial metrics from Yahoo Finance
2. **Applies Systematic Analysis**: 3-step framework (Valuation → Growth → Risk)
3. **Provides Clear Guidance**: BUY/HOLD/AVOID recommendations with confidence levels
4. **Shows Reasoning**: Chain-of-thought explanations for every decision

### 🏗️ Architecture:
Multi-Agent System Design:
┌─────────────────────────────────────────┐
│      Coordinating Agent (Main)          │
│  • Orchestrates workflow                │
│  • Synthesizes recommendations          │
│  • Chain-of-thought reasoning           │
└────────────┬────────────────────────────┘
             │
     ┌───────┴────────┬──────────────┐
     │                │              │
┌────▼─────┐  ┌──────▼─────┐  ┌────▼──────┐
│ Research │  │ Analysis   │  │Validation │
│  Agent   │  │   Agent    │  │  Agent    │
│          │  │            │  │           │
│• Data    │  │• Metrics   │  │• Quality  │
│  fetching│  │  calc.     │  │  checks   │
│• Screening│ │• Valuation │  │• Risk     │
│          │  │  analysis  │  │  flags    │
└──────────┘  └────────────┘  └───────────┘

---

### Technology Stack

- **Agent Framework**: Google ADK (Agent Development Kit)
- **LLM**: Gemini 2.5 Flash Lite
- **Data Sources**: Yahoo Finance API, Google Search
- **Memory System**: Conversational + User Profile tracking
- Observability: ADK LoggingPlugin
- **Evaluation**: Custom automated test suite
- **Language**: Python 3.11+

---


## ✨ Key Features

### ADK Capabilities Demonstrated (6/8 Required)

1. ✅ **Agent System**: Single coordinating agent with specialized reasoning
2. ✅ **Tools**: Custom (Yahoo Finance) + Built-in (Google Search)
3. ✅ **Chain-of-Thought**: Explicit 4-step reasoning framework
4. ✅ **Observability**: Full logging with LoggingPlugin
5. ✅ **Evaluation**: Automated test suite (85% pass rate)
6. ✅ **Context Engineering**: Structured prompts with clear instructions

### Advanced Features

- 🔄 **Session Memory**: Tracks user preferences across queries
- 🎯 **Multi-Stock Comparison**: Side-by-side analysis capability
- 📊 **Confidence Scoring**: High/Medium/Low confidence levels
- ⚠️ **Risk Assessment**: Automated red flag detection
- 📈 **Real-Time Data**: Live market integration
-🧪 **Automated Testing**: Evaluation framework with pass/fail metrics

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Google API Key (Gemini): [get one here](https://aistudio.google.com/app/apikey)

- Internet connection (for Yahoo Finance API)

### Installation
```bash
# 1. Clone the Repository
git clone https://github.com/yhernandez55/multi-agent-stock-analyzer.git
cd ai-investment-agent

# 2. Set Up Python Environment
python -m venv venv
# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API key
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
# .env file should look like:
# GOOGLE_API_KEY=AIzaSyC_your_actual_api_key_here
```

### Quick Start

#### Option 1: Run in Kaggle (Recommended)

1. Open the [Kaggle notebook](ai-financial-assistant.ipynb)
2. Click "Copy and Edit"
3. Go to "Add-ons" → "Secrets" → Add GOOGLE_API_KEY
4. Run all cells
5. Access the ADK Web UI via the generated proxy link

#### Option 2: Run Locally
```bash
# Test the agent programmatically
python runner/run_local_demo.py

# Or launch the ADK Web Interface optional
cd agent
adk web --log_level DEBUG
```

Visit `http://localhost:8000` and start testing!

---

## Testing:
```bash
python -c "
import asyncio
from demos.run_local_demo import runner
from evaluation.test_suite import run_evaluation
asyncio.run(run_evaluation(runner))
"
```

## 🙏 Acknowledgments

- **Google & Kaggle** - 5-Day AI Agents Intensive Course
- **Google ADK Team** - Excellent agent development framework
- **Yahoo Finance** - Reliable financial data API
- **Course Instructors** - Comprehensive agent architecture guidance

---

<div align="center">

**⭐ If you found this project helpful, please consider starring the repository! ⭐**

Made with ❤️ using [Google ADK](https://github.com/google/adk)

</div>
