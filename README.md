Capstone projects !

# PROJECT 1:
# Sales Brochure Generator (Gemini-powered)

This project is a Python-based AI application that automatically generates a **professional company brochure** for prospective customers, investors, and potential recruits.

Given a company name and its primary website, the system:
1. Scrapes the website
2. Uses an LLM to **reason about which pages are relevant**
3. Aggregates content from those pages
4. Generates a concise, high-quality brochure in Markdown

The project uses **Google Gemini models via the OpenAI-compatible API interface**, allowing OpenAI-style calls backed by Gemini.

---

## ✨ Features

- 🔍 Website scraping (landing page + relevant subpages)
- 🧠 LLM-based link selection (About, Careers, Company, etc.)
- 📝 AI-generated brochure content
- 🔄 Multi-step agent-style pipeline
- 🧱 Clean, modular `.py` project structure
- 🔐 Environment-based API key handling

---

## 🗂 Project Structure

sales-brochure-ai/
├── app/
│ ├── main.py # Entry point
│ ├── config.py # API keys & base URL
│ ├── brochure.py # Orchestration logic
│ ├── llms/
│ │ ├── gemini_openai_client.py
│ │ └── models.py
│ ├── web/
│ │ └── scraper.py
│ └── prompts/
│ ├── link_selector.py
│ └── brochure_writer.py
│
├── pyproject.toml
├── .gitignore
├── .env # Not committed
└── README.md

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sales-brochure-ai.git
cd sales-brochure-ai

2️⃣ Create and activate a virtual environment
uv venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

3️⃣ Install dependencies
uv sync


(or, if needed)

uv add openai python-dotenv requests beautifulsoup4 rich

4️⃣ Set up environment variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_gemini_api_key_here


⚠️ Never commit your .env file.

5️⃣ Run the application

From the project root:

python -m app.main


You should see a Markdown-formatted brochure printed in the terminal.

🧠 How It Works (High Level)

Scraping
The app fetches all links and text content from the company website.

Link Reasoning (LLM Call #1)
Gemini selects which links are relevant for a brochure.

Context Aggregation
Content from selected pages is combined into a single context.

Brochure Generation (LLM Call #2)
Gemini generates a polished brochure in Markdown.

This pattern is an early example of an agentic AI workflow using multiple LLM calls.

🛠 Tech Stack

Python 3.10+

uv (dependency & environment management)

Google Gemini (via OpenAI-compatible API)

openai Python SDK

requests + BeautifulSoup

rich for terminal rendering

🔐 Security Notes

.env is excluded via .gitignore

API keys are never hard-coded

Virtual environments (.venv) are not committed

📌 Roadmap / Next Improvements

Streaming brochure generation

FastAPI web service

HTML / PDF output

Industry-specific brochure templates

Gemini ↔ OpenAI model switching

Caching and rate limiting

📄 License

This project is for learning and experimentation purposes.
Add a license if you plan to distribute or commercialize it.

🙌 Acknowledgements

Built as a hands-on learning project to explore:

LLM orchestration

Prompt engineering

Agent-style AI workflows

Clean Python project structure


---

### ✅ What this README does well
- Explains **what** the project does
- Explains **how** it works
- Makes your repo instantly runnable
- Looks professional on GitHub
- Signals real-world engineering thinking

If you want next, I can:
- Shorten this for a portfolio README
- Add architecture diagrams
- Write a “Why this project?” section for recruiters
- Help you tag a **v0.1.0 release**

Just say the word 🚀