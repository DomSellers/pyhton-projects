import pandas as pd
from datetime import datetime
import os


FILENAME = "transactions.csv"

# Make sure the file exists (safety check)
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=["date", "category", "description", "amount"])
    df.to_csv(FILENAME, index=False)
    print("✅ Created new transactions.csv")
else:
    df = pd.read_csv(FILENAME)
    print("📂 Loaded existing transactions.csv")


def main_menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add a new transaction")
        print("2. View overall summary")
        print("3. View monthly summary")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_monthly_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")



def add_transaction():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (e.g. Food, Income, Bills): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount (negative for expense, positive for income): "))

    new_data = pd.DataFrame([[date, category, description, amount]], 
                            columns=["date", "category", "description", "amount"])
    new_data.to_csv(FILENAME, mode="a", header=False, index=False)
    print("✅ Transaction added successfully!")

def view_summary():
    df = pd.read_csv(FILENAME)

    if df.empty:
        print("No transactions found.")
        return

    total_income = df[df["amount"] > 0]["amount"].sum()
    total_expense = df[df["amount"] < 0]["amount"].sum()
    balance = total_income + total_expense

    print("\n--- Overall Summary ---")
    print(f"Total Income: £{total_income:.2f}")
    print(f"Total Expenses: £{abs(total_expense):.2f}")
    print(f"Net Balance: £{balance:.2f}")

    print("\nSpending by Category:")
    category_summary = df.groupby("category")["amount"].sum()
    print(category_summary)


def view_monthly_summary():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("No transactions found.")
        return

    month = input("Enter month (YYYY-MM): ")

    # Convert 'date' to datetime format
    df["date"] = pd.to_datetime(df["date"])
    df_filtered = df[df["date"].dt.strftime("%Y-%m") == month]

    if df_filtered.empty:
        print("No transactions for that month.")
        return

    total_income = df_filtered[df_filtered["amount"] > 0]["amount"].sum()
    total_expense = df_filtered[df_filtered["amount"] < 0]["amount"].sum()
    balance = total_income + total_expense

    print(f"\n--- Summary for {month} ---")
    print(f"Total Income: £{total_income:.2f}")
    print(f"Total Expenses: £{abs(total_expense):.2f}")
    print(f"Net Balance: £{balance:.2f}")

    print("\nSpending by Category:")
    category_summary = df_filtered.groupby("category")["amount"].sum()
    print(category_summary)


if __name__ == "__main__":
    main_menu()
