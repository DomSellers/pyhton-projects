#!/usr/bin/env python3
# warranty_rejection.py
# Generates a warranty rejection email based on reason (accidental damage or out of warranty)

from datetime import datetime, timedelta

def generate_email():
    print("\nWarranty Rejection Email Generator")
    print("----------------------------------\n")

    # Step 1: Ask which type of template to use
    print("Which type of rejection do you need?")
    print("1. Accidental damage")
    print("2. Out of warranty")
    choice = input("Enter 1 or 2: ").strip()

    # Validate user choice
    if choice not in ["1", "2"]:
        print("Invalid choice. Please restart and enter 1 or 2.")
        return

    # Step 2: Shared input
    account_number = input("Enter account number: ").strip().upper()
    frame_name = input("Enter frame name: ").strip()

    # Step 3: Accidental Damage Template
    if choice == "1":
        print("\nSelect a reason for rejection:")
        reasons = {
            "1": "Frame has clear signs of physical impact (bent or snapped).",
            "2": "Hinge damage consistent with misuse rather than manufacturing fault.",
            "3": "Lenses or frame damaged by excessive heat or chemical exposure.",
            "4": "Temple or bridge snapped under pressure.",
            "5": "Custom reason (enter your own text)"
        }

        for k, v in reasons.items():
            print(f"{k}. {v}")

        reason_choice = input("Select reason number: ").strip()

        if reason_choice in reasons and reason_choice != "5":
            reason_text = reasons[reason_choice]
        elif reason_choice == "5":
            reason_text = input("Enter your custom reason: ").strip()
        else:
            print("Invalid choice. Using custom reason.")
            reason_text = input("Enter your custom reason: ").strip()

        email = f"""
Subject: Warranty Claim – Accidental Damage – {frame_name}

Dear Sir/Madam,

Please note that this warranty claim for account {account_number} has been rejected due to suspected accidental damage.

Frame: {frame_name}

Reason:
    {reason_text}

To better assist you with the next steps, we have provided two options:

1. Return to Opticians:
Please let us know if you'd like the frame returning.
2. Eco-Friendly Recycling:
Alternatively, we can recycle the frame here at Eyespace on your behalf.


Best Regards,
Returns Department
"""

    # Step 4: Out of Warranty Template
    elif choice == "2":
        purchase_date_str = input("Enter purchase date (YYYY-MM-DD): ").strip()

        try:
            purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
            expiry_date = purchase_date + timedelta(days=18 * 30)  # approx. 18 months
            expiry_date_str = expiry_date.strftime("%Y-%m-%d")
        except ValueError:
            expiry_date_str = "Invalid date entered"

        reason_text = (
            "The claim has been rejected as the product is outside the 18-month manufacturer warranty period."
        )

        email = f"""
Subject: Warranty Claim – Out of Warranty – {frame_name}

Dear Customer,

Please note that this warranty claim for account {account_number} has been rejected as it is outside of the 18-month warranty period.

Frame: {frame_name}
Purchase date: {purchase_date_str}
Warranty expired on: {expiry_date_str}

Reason:
    {reason_text}


To better assist you with the next steps, we have provided two options:

1. Return to Opticians:
Please let us know if you'd like the frame returning.
2. Eco-Friendly Recycling:
Alternatively, we can recycle the frame here at Eyespace on your behalf.


Regards,
Dominic Sellers
Returns Department
"""

    # Step 5: Output
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
