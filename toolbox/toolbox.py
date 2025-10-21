import subprocess
import sys

def warranty_email_generator():
    subprocess.run([sys.executable, "framerejection.py"])
    input("\nPress Enter to return to the menu...")

def date_calculator():
    subprocess.run([sys.executable, "dateaddminus.py"])
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        print("\n=== Dominic's Python Toolbox ===")
        print("1. Warranty Email Generator")
        print("2. Date Adder/Subtractor")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            warranty_email_generator()
        elif choice == "2":
            date_calculator()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
