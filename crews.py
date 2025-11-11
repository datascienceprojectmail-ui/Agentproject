
from crewai import Crew, Process
from tasks import (
    sales_analysis_task,
    inventory_analysis_task,
    product_research_task,
    marketing_email_task,
)
from agents import sales_agent, inventory_agent, web_agent, marketing_agent

sales_crew = Crew(
    agents=[sales_agent],
    tasks=[sales_analysis_task],
    process=Process.sequential,
)

inventory_crew = Crew(
    agents=[inventory_agent],
    tasks=[inventory_analysis_task],
    process=Process.sequential,
)

product_crew = Crew(
    agents=[web_agent],
    tasks=[product_research_task],
    process=Process.sequential,
)

marketing_crew = Crew(
    agents=[marketing_agent],
    tasks=[marketing_email_task],
    process=Process.sequential,
)
