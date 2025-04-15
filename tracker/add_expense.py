import pandas as pd
import os
import json
from datetime import datetime

FILE = "expenses.json"

def run():
    amount = float(input("Amount: $"))
    category = input("Category (e.g., food, transport): ").strip()
    description = input("Description: ").strip()
    date = input("Date (YYYY-MM-DD or leave blank for today): ").strip()
    date = date or datetime.today().strftime('%Y-%m-%d')

    new_expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    if os.path.exists(FILE):
        df = pd.read_json(FILE)
        df = df._append(new_expense, ignore_index=True)
    else:
        df = pd.DataFrame([new_expense])

    df.to_json(FILE, orient="records", indent=2)
    print("✅ Expense added.")
