from datetime import datetime
from dateutil.relativedelta import relativedelta

# Ask user for the starting date
year = int(input("Enter the year (e.g. 2025): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

# Ask whether to add or subtract
choice = input("Do you want to add or subtract months? (enter 'add' or 'subtract'): ").strip().lower()

# Ask how many months to change
months = int(input("Enter the number of months: "))

# Create a date object
start_date = datetime(year, month, day)

# Perform the operation
if choice == "add":
    new_date = start_date + relativedelta(months=months)
    print("New date after adding", months, "months is:", new_date.strftime("%Y-%m-%d"))
elif choice == "subtract":
    new_date = start_date - relativedelta(months=months)
    print("New date after subtracting", months, "months is:", new_date.strftime("%Y-%m-%d"))
else:
    print("Invalid choice. Please enter 'add' or 'subtract'.")
