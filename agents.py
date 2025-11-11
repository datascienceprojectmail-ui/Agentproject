
import os
from dotenv import load_dotenv
from crewai import Agent
from tools import csv_tool, web_tool, email_tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    verbose=True,
    temperature=0.45,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

sales_agent = Agent(
    role="Sales Analyst",
    goal=(
        "Analyze sales.csv to produce sales trends, top-performing SKUs, "
        "seasonality signals, and recommended SKUs to promote."
    ),
    verbose=True,
    memory=True,
    backstory="An experienced retail sales analyst extracting business insights.",
    tools=[csv_tool],
    llm=llm,
    allow_delegation=False,
)

inventory_agent = Agent(
    role="Inventory Analyst",
    goal=(
        "Analyze inventory.csv (stock levels, lead times, turnover) recommend reorder quantities if on hand qty below reorder point recommend to restock"
    ),
    verbose=True,
    memory=True,
    backstory="A supply-chain focused analyst prioritizing SKU replenishment.",
    tools=[csv_tool],
    llm=llm,
    allow_delegation=False,
)

web_agent = Agent(
    role="Product Researcher",
    goal=(
        "Use web searches to gather product details, "
        "alternative SKUs and product pages for identified top SKUs."
    ),
    verbose=True,
    memory=True,
    backstory="An online researcher who finds product pages, alternatives and pricing.",
    tools=[web_tool],
    llm=llm,
    allow_delegation=False,
)

marketing_agent = Agent(
    role="Marketing & Email Agent",
    goal=(
        "Take sales insights, inventory recommendations, and product research "
        "and generate: (a) prioritized marketing campaigns, (b) personalized "
        "email content templates (subject, preheader, HTML/plain body), and "
        "(c) a sending plan (segment, cadence). Then send emails via the email tool." \
        "send emails to each customers personalised customer mails and names store in customers.csv"
    ),
    verbose=True,
    memory=True,
    backstory="A marketing automation specialist that crafts high-conversion emails.",
    tools=[email_tool,csv_tool],
    llm=llm,
    allow_delegation=False,
)
