import pandas as pd
import json
import os
from tabulate import tabulate

EXP_FILE = "expenses.json"
BUD_FILE = "budgets.json"

def run():
    if not os.path.exists(EXP_FILE) or not os.path.exists(BUD_FILE):
        print("Missing data. Add expenses and set budgets first.")
        return

    df = pd.read_json(EXP_FILE)
    with open(BUD_FILE, "r") as f:
        budgets = json.load(f)

    summary = []
    grouped = df.groupby("category")["amount"].sum()

    for category, budget in budgets.items():
        spent = grouped.get(category, 0.0)
        remaining = budget - spent
        summary.append({
            "Category": category,
            "Budget": f"${budget:.2f}",
            "Spent": f"${spent:.2f}",
            "Remaining": f"${remaining:.2f}"
        })

    print("\n📊 Budget Summary:\n")
    print(tabulate(summary, headers="keys", tablefmt="github"))
