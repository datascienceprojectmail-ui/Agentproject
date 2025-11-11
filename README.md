# Agentproject
CrewAI Retail Intelligence System

An intelligent multi-agent retail analysis and marketing automation platform powered by CrewAI and Gemini LLM.
It automatically analyzes sales data, forecasts inventory needs, performs product web research, and generates personalized marketing campaigns — including simulated email delivery.

🚀 Features
🧩 Modular AI Agents

Sales Analyst – Extracts sales trends, top-performing SKUs, and seasonality patterns.

Inventory Analyst – Detects low-stock SKUs, recommends reorder quantities, and restock priorities.

Product Researcher – Gathers product details and competitive alternatives from the web.

Marketing & Email Agent – Crafts marketing campaigns and sends customized emails to customers.

📊 Integrated Workflow

All agents collaborate in a hybrid multi-stage pipeline:

Sales, Inventory, and Web Research agents operate independently.

Their insights feed into the Marketing Agent for campaign generation.

🧰 Built-in Tools
Tool	Description
GeminiCSVTool	Analyzes CSVs (sales, inventory, customers) via Gemini LLM.
GeminiWebSearchTool	Summarizes online product research.
EmailSendTool	Simulates email sending by saving messages to /sent_emails/.
📁 Project Structure
📦 crewai-retail-intelligence
├── agents.py          # Defines all CrewAI agents with goals and tools
├── crews.py           # Creates Crew workflows for each functional area
├── tasks.py           # Defines the task logic and expected outputs
├── tools.py           # Custom Gemini-powered tools and email utility
├── datacreate.py      # Generates synthetic retail datasets
├── main.py            # Orchestrates the hybrid multi-agent workflow
└── data/
    ├── sales.csv
    ├── inventory.csv
    └── customers.csv

⚙️ Installation
1. Clone the Repository
git clone https://github.com/<your-username>/crewai-retail-intelligence.git
cd crewai-retail-intelligence

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

3. Install Dependencies
pip install -r requirements.txt




🔑 Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_google_gemini_api_key
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=you@example.com
EMAIL_PASS=yourpassword



data/sales.csv

data/inventory.csv

data/customers.csv

🧠 Run the Workflow

Execute the full retail intelligence pipeline:

python main.py


Output includes:

Sales insights

Inventory recommendations

Product research summaries

Marketing campaigns and generated email templates

Emails are saved in /sent_emails/.

🧩 Example Output
🚀 Starting Sales, Inventory, and Product Research stages...
✅ Sales Analysis Done.
✅ Inventory Analysis Done.
✅ Product Web Research Done.
📬 Running Marketing & Email Agent...
✅ Marketing step completed.
🎯 Final Results Summary printed to console

🧠 Tech Stack

Python 3.10+

CrewAI – Multi-agent coordination

LangChain + Gemini 2.0 – LLM reasoning and data analysis

Pandas – Data handling

dotenv – Config management

🧾 License

MIT License © 2025 — [Your Name or Organization]
