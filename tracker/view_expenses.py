import pandas as pd
import os
from tabulate import tabulate

FILE = "expenses.json"

def run():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    df = pd.read_json(FILE)
    df = df.sort_values("date", ascending=False)

    print("\n📄 All Expenses:\n")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
