#!/usr/bin/env python3
# warranty_rejection.py
# Generates a warranty rejection email based on reason (accidental damage or out of warranty)

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

print("Warranty Rejection Email Generator")
print("----------------------------------\n")

# Step 1: Ask which type of template to use
print("Which type of rejection do you need?")
print("1. Accidental damage")
print("2. Out of warranty")
choice = input("Enter 1 or 2: ").strip()

# Check user choice
if choice not in ["1", "2"]:
    print("Invalid choice. Please restart and enter 1 or 2.")
    exit()

# Step 2: Shared input
account_number = input("Enter account number: ").strip().upper()
frame_name = input("Enter frame name: ").strip()
# Step 3: Accidental Damage Template
if choice == "1":
    reason_text = input("Enter the reason for rejection: ")
    
    email = f"""
Subject: Warranty Claim – Accidental Damage – {frame_name}

Dear Customer,

Please note that this warranty claim for account {account_number} has been rejected for suspected accidental damage reasons. Please see below for further details.

Frame: {frame_name}

Reason:
    {reason_text}


Please let us know if you would like this frame returning to you, or if you would like us to recycle the frame on your behalf.

Regards,
[Your Name]
[Your Department]
"""

# Step 4: Out of Warranty Template
elif choice == "2":
    purchase_date_str = input("Enter purchase date (YYYY-MM-DD): ").strip()
    
    try:
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        cutoff_date = purchase_date + relativedelta(months=+18)  # roughly 18 months
        cutoff_date_str = cutoff_date.strftime("%Y-%m-%d")
    except ValueError:
        cutoff_date_str = "Invalid date entered"
    
    reason_text = (
        "The claim has been rejected as the product is outside the 18-month manufacturer warranty period."
    )
    
    email = f"""
Subject: Warranty Claim – Out of Warranty – {frame_name}

Dear Customer,

Please note that this warranty claim for account {account_number} has been rejected as it is outside of the 18-month warranty period.

Frame: {frame_name}
Purchase date: {purchase_date_str}
Warranty expired on: {cutoff_date_str}

Reason:
    {reason_text}

Regards,
[Your Name]
[Your Department]
"""

# Step 5: Output
print("\n----------------------------------")
print("Generated Email:\n")
print(email)
print("----------------------------------")
print("Done - Copy and paste this email into your email application.")
