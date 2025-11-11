
import os
import json
from dotenv import load_dotenv
from crews import sales_crew, inventory_crew, product_crew, marketing_crew

load_dotenv()

def extract_output(result):
    """Safely extract string/dict from CrewOutput objects."""
    try:
        if hasattr(result, "raw_output") and result.raw_output:
            return result.raw_output
        elif hasattr(result, "output") and result.output:
            return result.output
        elif isinstance(result, (str, dict, list)):
            return result
        else:
            return str(result)
    except Exception:
        return str(result)

def run_hybrid_workflow():
    print("🚀 Starting Sales, Inventory, and Product Research stages (independent)...\n")

    base_inputs = {
        "sales_csv": os.getenv("SALES_CSV", "sales.csv"),
        "inventory_csv": os.getenv("INVENTORY_CSV", "inventory.csv"),
        "customer_csv": os.getenv("CUSTOMER_CSV", "customers.csv"),
    }

    # ---  Sales Analysis ---
    print("📊 Running Sales Analysis...")
    sales_result = sales_crew.kickoff(inputs=base_inputs)
    print("✅ Sales Analysis Done.\n")

    # ---  Inventory Analysis ---
    print("📦 Running Inventory Analysis...")
    inventory_result = inventory_crew.kickoff(inputs=base_inputs)
    print("✅ Inventory Analysis Done.\n")

    # ---  Product Research ---
    print("🌐 Running Product Web Research...")
    product_result = product_crew.kickoff(inputs=base_inputs)
    print("✅ Product Web Research Done.\n")

    sales_text = extract_output(sales_result)
    inventory_text = extract_output(inventory_result)
    product_text = extract_output(product_result)

    combined_inputs = {
        "topic": "Retail marketing campaign generation",
        "sales_insights": sales_text,
        "inventory_recommendations": inventory_text,
        "product_research": product_text,
        "customer_csv": base_inputs["customer_csv"],
    }

    # ---  Marketing & Email ---
    print("📬 Running Marketing & Email Agent with full context...")
    marketing_result = marketing_crew.kickoff(inputs=combined_inputs)
    print("✅ Marketing step completed.\n")

    print("=== Final Results Summary ===")
    try:
        print(json.dumps({
            "sales_result": sales_text,
            "inventory_result": inventory_text,
            "product_result": product_text,
            "marketing_result": extract_output(marketing_result),
        }, indent=2))
    except Exception:
        print("Sales:", sales_text)
        print("Inventory:", inventory_text)
        print("Product:", product_text)
        print("Marketing:", marketing_result)

if __name__ == "__main__":
    run_hybrid_workflow()
