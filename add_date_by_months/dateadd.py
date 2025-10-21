

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Ask user for the starting date
year = int(input("Enter the year (e.g. 2025): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

# Ask how many months to add
months_to_add = int(input("Enter number of months to add: "))

# Create a date object
start_date = datetime(year, month, day)

# Add months using relativedelta
new_date = start_date + relativedelta(months=months_to_add)

# Display result
print("New date after adding", months_to_add, "months is:", new_date.strftime("%Y-%m-%d"))
