# 📈 AI Stock Screener

> A lightweight, rule-based stock screening workflow built with **LangGraph** and **Yahoo Finance**.

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-1C3C3C?logo=langchain\&logoColor=white)](https://www.langchain.com/langgraph)
[![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-6001D2?logo=yahoo\&logoColor=white)](https://finance.yahoo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

**AI Stock Screener** is a lightweight stock screening application that combines **LangGraph's graph-based workflow orchestration** with **Yahoo Finance market data**.

The application retrieves stocks using predefined Yahoo Finance screeners, evaluates the returned stocks using a transparent rule-based scoring system, and generates a ranked terminal report.

The project was deliberately designed to be:

* ⚡ Lightweight
* 🧩 Modular
* 🔍 Explainable
* 💻 Easy to run locally
* 🧠 Ready for future LLM integration
* 📚 Beginner-friendly while demonstrating real agent/workflow concepts

> **Current version:** This project does **not** require a local or cloud LLM.
> The current implementation is a deterministic LangGraph workflow. LLM-based natural-language screening is planned as a future version.

---

## ✨ Features

### 📊 Yahoo Finance Stock Screening

Retrieve real-time market data through Yahoo Finance's predefined screeners.

Supported screeners include:

* `day_gainers`
* `day_losers`
* `most_actives`
* `growth_technology_stocks`
* `undervalued_growth_stocks`
* `undervalued_large_caps`
* `small_cap_gainers`
* `most_shorted_stocks`

Additional screeners supported by the underlying Yahoo Finance interface may also be available depending on the installed `yfinance` version.

---

### 🧮 Rule-Based Stock Ranking

Each retrieved stock is assigned a simple score based on available market information.

The current scoring system considers:

#### 52-Week Price Position

The system calculates where the current price lies between the 52-week low and high:

```text
Position = (Current Price - 52-Week Low)
           --------------------------------
           (52-Week High - 52-Week Low)
```

Stocks closer to the lower part of their 52-week range receive additional points.

#### Analyst Rating

Stocks with analyst ratings such as:

* Strong Buy
* Buy

receive additional points.

This produces a transparent ranking rather than an opaque prediction.

---

### 🔗 LangGraph Workflow

The application uses LangGraph to represent the processing pipeline as a graph:

```text
                  ┌──────────────┐
                  │     START    │
                  └──────┬───────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Fetch Stocks   │
                │  Yahoo Finance  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Rank Results   │
                │ Rule-Based Score│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Create Report   │
                └────────┬────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │      END     │
                  └──────────────┘
```

This separates data retrieval, analysis, and presentation into independent stages.

---

## 🏗️ Architecture

The project follows a simple modular architecture:

```text
User
 │
 │ Select screener
 ▼
┌─────────────────────┐
│      LangGraph      │
│    State Machine    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Yahoo Finance    │
│     Data Fetcher    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Stock Ranking    │
│  Rule-Based Engine  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Report Builder   │
└──────────┬──────────┘
           │
           ▼
      Terminal Output
```

### Project Components

| File               | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| `flow.py`          | Defines and executes the LangGraph workflow      |
| `tools.py`         | Retrieves stock data from Yahoo Finance          |
| `screener.py`      | Contains the ranking and report-generation logic |
| `pyproject.toml`   | Project metadata and dependencies                |
| `uv.lock`          | Reproducible dependency lockfile                 |
| `graphdiagram.png` | Architecture/workflow diagram                    |

---

## 🧠 Why LangGraph?

A simple Python script could perform the same three operations sequentially.

However, LangGraph provides a structured way to represent application logic as a graph of nodes and state transitions.

The project therefore demonstrates concepts that become useful when the system grows into a more sophisticated agent:

```text
Current

START
  ↓
Fetch
  ↓
Analyze
  ↓
Report
  ↓
END


Future

START
  ↓
Understand User Request
  ↓
Choose Tools
  ↓
Fetch Market Data
  ↓
Analyze
  ↓
Validate
  ↓
Generate Explanation
  ↓
END
```

The current implementation intentionally keeps the architecture simple instead of adding unnecessary LLM dependencies.

---

## 🛠️ Tech Stack

### Core

* **Python 3.13+**
* **LangGraph**
* **yfinance**

### Dependency Management

* **uv**

### Data Source

* **Yahoo Finance**

### Current AI/LLM Dependency

**None.**

The project currently uses deterministic logic rather than an LLM.

This keeps the application:

* smaller
* cheaper
* easier to reproduce
* easier to debug
* easier to understand

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-stock-screener.git
cd ai-stock-screener
```

Replace `YOUR_USERNAME` with your GitHub username.

---

### 2. Install UV

If UV is not already installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal after installation if required.

Verify:

```bash
uv --version
```

---

### 3. Install dependencies

From the project directory:

```bash
uv sync
```

This creates the project's virtual environment and installs the required dependencies.

---

## ▶️ Running the Application

Run:

```bash
uv run flow.py
```

You should see:

```text
============================================================
             AI STOCK SCREENER
============================================================

Available screeners:

1. day_gainers
2. day_losers
3. most_actives
4. growth_technology_stocks
5. undervalued_growth_stocks
6. undervalued_large_caps
7. small_cap_gainers
8. most_shorted_stocks

Enter screener:
```

For example:

```text
Enter screener: day_gainers
```

The application retrieves market data and produces a ranked report.

Example:

```text
================================================================================
STOCK SCREENING RESULTS
================================================================================

 1. VST      Vistra Corp.                    Price: 168.42       Score: 5
 2. WCC      Wesco International             Price: 302.15       Score: 3
 3. VSH      Vishay Intertechnology          Price: 25.91        Score: 3

================================================================================
Rule-based screening only — NOT financial advice.
```

> Prices and rankings are examples. Actual results change with live market data.

---

## 🔍 How It Works

### Step 1 — User selects a screener

The user enters a predefined Yahoo Finance screener:

```text
day_gainers
```

---

### Step 2 — LangGraph initializes the workflow

The selected screener is stored in the graph state.

The state contains:

```python
class State(TypedDict):
    screen_type: str
    stocks: list[dict]
    ranked_stocks: list[dict]
    report: str
```

---

### Step 3 — Fetch market data

`tools.py` accesses Yahoo Finance through `yfinance`.

The application retrieves information such as:

* Symbol
* Company name
* Exchange
* Current market price
* Market capitalization
* 52-week high
* 52-week low
* Analyst rating

---

### Step 4 — Rank stocks

`screener.py` applies deterministic scoring rules.

The important point is that the ranking logic is:

> **transparent and reproducible**

There is no hidden model deciding the score.

---

### Step 5 — Generate the report

The ranked data is converted into a readable terminal report.

The final output is returned through the LangGraph state.

---

## 📁 Project Structure

```text
ai-stock-screener/
│
├── flow.py
│
├── tools.py
│
├── screener.py
│
├── graphdiagram.png
│
├── README.md
│
├── pyproject.toml
│
├── uv.lock
│
└── .gitignore
```

---

## 🔬 Design Decisions

### Why no local LLM?

The original tutorial that inspired this project used a locally hosted Ollama model.

For this implementation, the local LLM dependency was intentionally removed.

This means the project does not require:

* Ollama
* Downloading a multi-GB model
* GPU memory
* Large model files
* API keys

The result is a much smaller and more reproducible project.

---

### Why use LangGraph without an LLM?

LangGraph is useful for more than just LLM agents.

It provides graph-based state management and workflow orchestration.

Using it here creates a clean foundation for future extensions while keeping the first version deterministic.

---

### Why rule-based scoring?

A rule-based scoring system makes the application's decisions easy to inspect.

For example:

```text
52-week position
        +
analyst rating
        ↓
    score
        ↓
    ranking
```

This is preferable for the initial version because it avoids pretending that a simple LLM-generated opinion is a reliable financial signal.

---

## 🚀 Roadmap

The project is intentionally designed to evolve.

### Version 1 — Current

**Lightweight LangGraph stock screening workflow**

* [x] Yahoo Finance integration
* [x] Predefined screeners
* [x] LangGraph workflow
* [x] Deterministic stock scoring
* [x] Terminal report
* [x] No local AI model required
* [x] Minimal dependencies

---

### Version 2 — Natural Language Interface

Add an optional cloud LLM.

Example:

```text
User:

"Show me technology stocks that are currently
near their 52-week lows."
```

The LLM would translate the request into structured screening parameters.

---

### Version 3 — Agentic Tool Selection

Allow the model to choose between multiple tools:

```text
                 User
                   │
                   ▼
            ┌─────────────┐
            │     LLM     │
            └──────┬──────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     Screener    Quotes     News
        │          │          │
        └──────────┼──────────┘
                   ▼
               Analysis
                   │
                   ▼
                Report
```

---

### Version 4 — Web Interface

Build a browser-based dashboard with:

* Stock tables
* Interactive filtering
* Charts
* Search
* Screener selection
* Natural-language queries
* Portfolio watchlists

Potential stack:

```text
Next.js
   +
FastAPI
   +
LangGraph
   +
Yahoo Finance
```

---

### Version 5 — Production-Oriented System

Potential additions:

* Caching
* Error handling
* Rate-limit handling
* Logging
* Automated tests
* Persistent state
* Multiple market-data providers
* News sentiment
* Fundamental analysis
* Technical indicators
* Backtesting

---

## ⚠️ Limitations

This project is a **software engineering and learning project**, not a professional investment system.

The current implementation:

* does not predict future stock prices
* does not perform complete fundamental analysis
* does not guarantee returns
* does not account for an investor's risk profile
* does not perform portfolio optimization
* does not provide personalized investment advice
* relies on data availability from Yahoo Finance
* uses a deliberately simple scoring model

Market data may also change between executions.

---

## 💰 Financial Disclaimer

> **This project is for educational and software-development purposes only. It is not financial advice.**

The ranking score is a demonstration of rule-based data processing and should **not** be interpreted as a recommendation to buy, sell, or hold any security.

Always conduct independent research and consult a qualified financial professional before making investment decisions.

---

## 🧪 Testing

Basic syntax validation can be performed with:

```bash
uv run python -m py_compile flow.py tools.py screener.py
```

You can also test the Yahoo Finance data retrieval independently:

```bash
uv run python -c "from tools import get_stocks; print(get_stocks('day_gainers'))"
```

---

## 🔧 Troubleshooting

### `uv: command not found`

Install UV:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then restart the terminal.

---

### Yahoo Finance request fails

The application depends on Yahoo Finance being accessible.

Try again later if the service temporarily rejects a request.

---

### Invalid screener

Make sure the screener name is entered exactly, for example:

```text
day_gainers
```

rather than:

```text
Day Gainers
```

---

## 📚 Learning Objectives

This project was built to explore:

* Python project structure
* Dependency management with UV
* LangGraph fundamentals
* Graph-based workflows
* Typed application state
* API/data-source integration
* Data transformation
* Rule-based ranking
* Modular architecture
* Git/GitHub project management
* Designing systems that can later incorporate LLMs

---

## 🎯 What This Project Demonstrates

From a software-engineering perspective, the project demonstrates a simple but extensible pipeline:

```text
External Data
     ↓
Data Retrieval
     ↓
State Management
     ↓
Business Logic
     ↓
Ranking
     ↓
Presentation
```

The architecture deliberately separates these responsibilities so that individual components can later be replaced without rewriting the entire application.

For example:

```text
Yahoo Finance
     ↓
     X
     ↓
Polygon / Alpha Vantage / another provider
```

or:

```text
Rule-Based Ranking
        ↓
        X
        ↓
ML / LLM-assisted Analysis
```

without fundamentally changing the overall workflow structure.

---

## 🌱 Inspiration & Attribution

This project was **inspired by the LangGraph Crash Course by Nick Nochnack**.

The original tutorial served as a learning reference for understanding LangGraph, tool-based workflows, and stock screening.

This repository was subsequently restructured into an independent lightweight implementation with:

* a different dependency structure
* removal of the local Ollama model
* a deterministic ranking system
* a simplified architecture
* separate data-fetching and screening modules
* a new project structure
* an independent development roadmap

Original learning reference:

**LangGraph Crash Course — Nick Nochnack**

https://github.com/nicknochnack/LanggraphCrashCourse

The purpose of the attribution is to clearly acknowledge the educational source that helped initiate the project.

---

## 📌 Portfolio Context

This project is part of my exploration of:

* Artificial Intelligence
* Machine Learning
* Data Science
* LLM applications
* Agentic systems
* Graph-based AI workflows

The current version focuses on building a clean foundation before introducing additional AI complexity.

---

## 👨‍💻 Author

**Barnik Basu**

Computer Science & Engineering
IIIT Kalyani

Interested in:

```text
AI / ML
Data Science
LLMs
Agentic AI
Research
Software Engineering
```

---

## ⭐ Future Vision

The long-term goal is to evolve this project from a simple deterministic screening workflow into an **explainable financial research assistant**.

The intended evolution is:

```text
             CURRENT
                │
                ▼
      Rule-Based Screener
                │
                ▼
       LangGraph Workflow
                │
                ▼
        Natural Language
                │
                ▼
         Multiple Tools
                │
                ▼
       AI-Assisted Research
                │
                ▼
      Explainable Dashboard
```

The emphasis will remain on **transparent reasoning, modular architecture, reproducibility, and responsible use of financial data**.

---

## 📄 License

This project is released under the **MIT License**.

See `LICENSE` for details.

---

<p align="center">
  Built with Python, LangGraph & Yahoo Finance
</p>
