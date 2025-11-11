
from crewai import Task
from agents import sales_agent, inventory_agent, web_agent, marketing_agent
from tools import csv_tool, web_tool, email_tool

sales_analysis_task = Task(
    description="Analyze sales.csv to produce insights and top SKUs.",
    expected_output="Sales insights (top SKUs, segments, trends) as JSON/text summary.",
    tools=[csv_tool],
    agent=sales_agent,
)

inventory_analysis_task = Task(
    description="Analyze inventory.csv to determine stock levels and reorder needs.",
    expected_output="Inventory recommendations (reorder SKUs/quantities/urgency) as JSON.",
    tools=[csv_tool],
    agent=inventory_agent,
)

product_research_task = Task(
    description="Search the web for some ecommerce products and alternatives.",
    expected_output="List of product  and short summaries (per SKU).",
    tools=[web_tool],
    agent=web_agent,
)

marketing_email_task = Task(
    description=(
        "Using outputs from sales, inventory and product research, "
        "build marketing campaigns, generate email templates per segment/SKU, the email sent should include actual not placeholders "
        "and send emails via SMTP/email tool.send to "
    ),
    expected_output="Campaign plan, generated email bodies (HTML/plain), and send/log confirmation.",
    tools=[email_tool],
    agent=marketing_agent,
)
