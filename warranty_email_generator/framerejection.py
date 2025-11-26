#!/usr/bin/env python3
# warranty_rejection.py
# This script generates a generic rejection email for either either an expired warranty or accidental damage case.

from datetime import datetime, timedelta

def generate_email():
    print("\nWarranty Rejection Email Generator")
    print("----------------------------------\n")

    # Ask which type of template to use
    print("Which type of rejection do you need?")
    print("1. Accidental damage")
    print("2. Out of warranty")
    choice = input("Enter 1 or 2: ").strip()

    # Validate user choice
    if choice not in ["1", "2"]:
        print("Invalid choice. Please restart and enter 1 or 2.")
        return

    # Shared input
    account_number = input("Enter name/account: ").strip().upper()
    product_name = input("Enter product name: ").strip()

    # Accidental Damage Template
    if choice == "1":


        reason_text = input("Enter your custom reason: ").strip()


        email = f"""
Subject: Warranty Claim – Accidental Damage – {frame_name}

Dear Sir/Madam,

Thank you for sending in the frame for assessment. After carefully reviewing the item linked to account {account_number}, we’re unable to accept the claim under warranty as the damage appears to be the result of accidental impact rather than a manufacturing fault.

Frame: {product_name}

Reason for rejection:
    {reason_text}



"""

    # Out of Warranty Template
    elif choice == "2":
        purchase_date_str = input("Enter purchase date (YYYY-MM-DD): ").strip()

        try:
            purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
            expiry_date = purchase_date + timedelta(days=18 * 30)  
            expiry_date_str = expiry_date.strftime("%Y-%m-%d")
        except ValueError:
            expiry_date_str = "Invalid date entered"

        reason_text = (
            "The claim has been rejected as the product is outside the 18-month manufacturer warranty period."
        )

        email = f"""
Subject: Warranty Claim – Out of Warranty – {product_name}

Dear Customer,

Please note that this warranty claim for account {account_number} has been rejected as it is outside of the 18-month warranty period.

Product: {product_name}
Purchase date: {purchase_date_str}
Warranty expired on: {expiry_date_str}

Reason:
    {reason_text}


Best Regards,

"""

    # Output
    print("\n----------------------------------")
    print("Generated Email:\n")
    print(email)
    print("----------------------------------")
    print("Done - Copy and paste this email into your email client.\n")


# --- Main Loop ---
while True:
    generate_email()
    again = input("Would you like to generate another email? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break
