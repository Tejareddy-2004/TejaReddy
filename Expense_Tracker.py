import os
import csv

# Global list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    item = input("Enter expense item description: ")
    
    while True:
        amount_str = input("Enter the expense amount: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Please enter a valid numeric amount.")

    expenses.append({"date": date, "item": item, "amount": amount})
    print("Expense added successfully!\n")

# Function to view total expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    print("\n--- Expense Records ---")
    print(f"{'Date':<12} {'Item':<20} {'Amount'}")
    print("-" * 40)
    
    total = 0
    for exp in expenses:
        print(f"{exp['date']:<12} {exp['item']:<20} {exp['amount']}")
        total += exp['amount']
    
    print("-" * 40)
    print(f"Total Expenses: {total:.2f}\n")

# Function to calculate weekly average expenses
def calculate_weekly_average():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total_expenses = sum(exp["amount"] for exp in expenses)
    num_weeks = len(set(exp["date"][:7] for exp in expenses))
    avg_weekly = total_expenses / max(1, num_weeks)

    print(f"\nTotal Expenses: {total_expenses:.2f}")
    print(f"Number of Weeks Tracked: {num_weeks}")
    print(f"Average Weekly Expenses: {avg_weekly:.2f}\n")

# Function to provide expense minimization tips
def expense_minimization_tips():
    tips = [
        "1. Track your expenses daily.",
        "2. Set a monthly budget and stick to it.",
        "3. Prioritize needs over wants.",
        "4. Avoid unnecessary subscriptions.",
        "5. Use discount coupons and cashback offers."
    ]
    print("\n--- Expense Minimization Tips ---")
    for tip in tips:
        print(tip)
    print("\n")

# Function to save expenses to internal storage
def save_expenses():
    if not expenses:
        print("No expenses recorded yet to save.\n")
        return
    
    # Define folder and file path
    folder_path = "/storage/emulated/0/ExpenseTracker"
    file_path = os.path.join(folder_path, "expenses.csv")

    # Create directory if not exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Write to CSV file
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Item", "Amount"])
        for exp in expenses:
            writer.writerow([exp["date"], exp["item"], exp["amount"]])

    print(f"Expenses saved successfully at: {file_path}\n")

# Main menu function
def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add an Expense")
        print("2. View Total Expenses")
        print("3. Get Expense Minimization Tips")
        print("4. Calculate Weekly Average Expenses")
        print("5. Exit")
        print("6. Save Expenses Data")

        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_minimization_tips()
        elif choice == '4':
            calculate_weekly_average()
        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        elif choice == '6':
            save_expenses()
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
    
def calculate_weekly_average():
    if not expenses:
        print("No expenses recorded yet to calculate weekly average.\n")
        return

    print(f"\nTotal Expenses: {total_expense:.2f}")
    print(f"Number of Weeks Tracked: {len(expenses) // 7 if len(expenses) >= 7 else 1}")
    print(f"Average Weekly Expenses: {weekly_avg:.2f}\n")  # Show loaded weekly avg
    
def load_expenses():
    global expenses, total_expense, weekly_avg
    folder_path = "/storage/emulated/0/ExpenseTracker"
    file_path = os.path.join(folder_path, "expenses.json")

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            expenses = data.get("expenses", [])
            total_expense = data.get("total_expenses", 0)
            weekly_avg = data.get("weekly_average", 0)
            print("Previous expenses, total, and weekly average loaded successfully!\n")
        except json.JSONDecodeError:
            print("Error: Corrupt JSON file. Data might be lost.\n")
            expenses = []
            total_expense = 0
            weekly_avg = 0
    else:
        print("No previous data found. Starting fresh.\n")
        expenses = []
        total_expense = 0
        weekly_avg = 0
        
import os
import json

def save_expenses():
    if not expenses:
        print("No expenses recorded yet to save.\n")
        return
    
    folder_path = "/storage/emulated/0/ExpenseTracker"
    file_path = os.path.join(folder_path, "expenses.json")

    # Ensure the directory exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Calculate total expenses
    total_expense = sum(exp["amount"] for exp in expenses)

    # Calculate weekly average expenses
    if len(expenses) > 0:
        num_weeks = (len(expenses) / 7) if len(expenses) >= 7 else 1
        weekly_avg = total_expense / num_weeks
    else:
        weekly_avg = 0

    # Save all data in JSON format
    data_to_save = {
        "expenses": expenses,
        "total_expenses": total_expense,
        "weekly_average": weekly_avg
    }

    try:
        with open(file_path, "w") as file:
            json.dump(data_to_save, file, indent=4)
        print(f"✅ Expenses, total, and weekly average saved successfully at: {file_path}\n")
    except Exception as e:
        print(f"Error saving expenses: {e}\n")