import json
import os

FILE = "budgets.json"

def run():
    category = input("Category to set/update budget: ").strip()
    amount = float(input(f"Budget for {category}: $"))

    budgets = {}
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            budgets = json.load(f)

    budgets[category] = amount

    with open(FILE, "w") as f:
        json.dump(budgets, f, indent=2)

    print("✅ Budget set.")

