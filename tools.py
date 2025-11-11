
import os
from dotenv import load_dotenv
from crewai_tools import (
    CSVSearchTool,
    WebsiteSearchTool,
    FirecrawlScrapeWebsiteTool,
)
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import pandas as pd
from dotenv import load_dotenv
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    verbose=True,
    temperature=0.4,
    google_api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiCSVToolInput(BaseModel):
    """Schema for CSV Analysis Tool input."""
    file_path: str = Field(..., description="Path to the CSV file to analyze.")
    question: str = Field(..., description="Natural language query about the CSV content.")


class GeminiCSVTool(BaseTool):
    """A tool that loads CSV data and uses Gemini to analyze or query it."""
    name: str = "GeminiCSVAnalyzerTool"
    description: str = (
        "Analyze structured CSV files using Gemini. "
        "Useful for asking questions about csv data."
    )
    args_schema: Type[BaseModel] = GeminiCSVToolInput

    def _run(self, file_path: str, question: str) -> str:
        try:
            # Load and summarize the CSV
            if not os.path.exists(file_path):
                return f"❌ File not found: {file_path}"

            df = pd.read_csv(file_path)
            sample = df.to_string()
            summary = f"The CSV file has {len(df)} rows and {len(df.columns)} columns. Columns: {list(df.columns)}"

            # Construct prompt for Gemini
            prompt = f"""
            You are a retail data analyst.
            {summary}

            Here are the available knowledge
            {sample}

            Question: {question}

            Provide a clear and concise analysis or answer.
            """

            response = llm.invoke(prompt)
            return response.content if hasattr(response, "content") else str(response)
        except Exception as e:
            return f"⚠️ Gemini CSV Tool error: {e}"


class GeminiWebToolInput(BaseModel):
    """Schema for web search."""
    query: str = Field(..., description="Search query about  products or competitors.")


class GeminiWebSearchTool(BaseTool):
    name: str = "GeminiWebSearchTool"
    description: str = "Search for  related products using Gemini reasoning."
    args_schema: Type[BaseModel] = GeminiWebToolInput

    def _run(self, query: str) -> str:
        prompt = f"Search the web and summarize key information about: {query}"
        try:
            result = llm.invoke(prompt)
            return result.content if hasattr(result, "content") else str(result)
        except Exception as e:
            return f"⚠️ Gemini Web Tool error: {e}"


class EmailToolInput(BaseModel):
    """Input schema for the email tool"""
    to_email: str = Field(..., description="Recipient's email address.")
    subject: str = Field(..., description="Subject of the email.")
    body: str = Field(..., description="Body text or HTML content.")
    html: bool = Field(default=False, description="Set True to send HTML email.")


class EmailSendTool(BaseTool):
    name: str = "EmailSendTool"
    description: str = (
        "Send emails using SMTP credentials in environment variables: "
        "EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASS."
    )
    args_schema: Type[BaseModel] = EmailToolInput

    def _run(self, to_email: str, subject: str, body: str, html: bool = False) -> str:
        """
        Simulates sending an email by saving the email content to a .txt file
        instead of actually sending via SMTP.
        """
        try:
            os.makedirs("sent_emails", exist_ok=True)

            safe_subject = "".join(c if c.isalnum() or c in (" ", "_", "-") else "_" for c in subject)
            filename = f"sent_emails/{to_email.replace('@', '_at_')}_{safe_subject[:50]}.txt"

            content = (
                f"To: {to_email}\n"
                f"Subject: {subject}\n"
                f"Format: {'HTML' if html else 'Plain Text'}\n"
                f"{'-'*60}\n"
                f"{body}\n"
            )

            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

            return f"✅ Email saved to {filename}"

        except Exception as e:
            return f"⚠️ Error saving email: {e}"

        

csv_tool = GeminiCSVTool()
web_tool = GeminiWebSearchTool()
email_tool = EmailSendTool()
