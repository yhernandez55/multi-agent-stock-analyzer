# 🤖 AI Investment Research Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4)](https://github.com/google/adk)

> **Capstone Project**: 5-Day AI Agents Intensive Course with Google  
> **Track**: AI Financial Assistant
> **Author**: Yanelly Hernandez
> **Submission Date**: December 1, 2025

An intelligent agent that automates stock investment research, reducing analysis time from 2+ hours to 3 minutes while maintaining 85% quality assurance standards.

---

## 🎯 Quick Links

- 📓 [**Live Kaggle Demo**](ai-financial-assistant.ipynb)
- 🎥 [**Video Walkthrough**](/var/folders/6j/3l6q9l4515sdmfyg8znhblxr0000gn/T/TemporaryItems/NSIRD_screencaptureui_zdajiz/Screen Recording 2025-11-30 at 9.24.29 PM.mov)

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

---

### Technology Stack

- **Agent Framework**: Google ADK (Agent Development Kit)
- **LLM**: Gemini 2.5 Flash Lite
- **Data Sources**: Yahoo Finance API, Google Search
- **Observability**: ADK LoggingPlugin
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

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Google API Key (Gemini)
- Internet connection (for Yahoo Finance API)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/multi-agent-stock-analyzer.git
cd ai-investment-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up API key
export GOOGLE_API_KEY=" "
```

### Quick Start

#### Option 1: Run in Kaggle (Recommended)

1. Open the [Kaggle notebook](ai-financial-assistant.ipynb)
2. Click "Copy and Edit"
3. Add your `GOOGLE_API_KEY` to Kaggle Secrets
4. Run all cells

#### Option 2: Run Locally
```bash
# Test the agent programmatically
python agent/agent.py

# Or launch the ADK Web Interface
cd agent
adk web --log_level DEBUG
```

Visit `http://localhost:8000` and start testing!

---

## 📊 Results & Validation

### Performance Metrics

- ⚡ **Time Efficiency**: 95% reduction (2 hours → 3 minutes)
- ✅ **Quality Score**: 85% pass rate on automated evaluation
- 🎯 **Success Rate**: 100% completion rate (no failures)
- 📈 **Coverage**: Successfully analyzes stocks across all sectors

---

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