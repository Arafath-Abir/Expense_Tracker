import csv
import os

FILE_NAME = "expenses.csv"

# Functions
def add_expense(amount, category, description):
    """Add an expense to the CSV file."""
    file_exists = os.path.isfile(FILE_NAME)
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Amount", "Category", "Description"])
        writer.writerow([amount, category, description])
    print(f"✅ Expense added: {amount} | {category} | {description}")

def show_expenses():
    """Show all expenses."""
    if not os.path.isfile(FILE_NAME):
        print("❌ No expenses recorded yet.")
        return
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def total_expense():
    """Show total expense amount."""
    if not os.path.isfile(FILE_NAME):
        print("❌ No expenses recorded yet.")
        return
    total = 0
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f"💰 Total Expense: {total}")

# CLI Program
def main():
    print("=== Simple Expense Tracker ===")
    while True:
        print("\nMenu:\n1) Add Expense\n2) Show All Expenses\n3) Show Total Expense\n4) Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            amount = input("Enter amount: ").strip()
            category = input("Enter category (Food, Transport, etc.): ").strip()
            description = input("Enter description: ").strip()
            add_expense(amount, category, description)
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Exiting. Thank you! ✨")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
