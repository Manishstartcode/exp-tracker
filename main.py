import tracker
from tracker import add_expense, view_expenses, set_budget, view_budget

def main():
    while True:
        print("\n💸 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. View Budget Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_expense.run()
        elif choice == "2":
            tracker.view_expenses.run()
        elif choice == "3":
            tracker.set_budget.run()
        elif choice == "4":
            tracker.view_budget.run()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
