expenses = []

def main():
    while True:
        print("\nWelcome to the Expense Tracker ")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Update Expense")
        print("4. Remove Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        # Viewing Expenses
        if choice == "1":
            if not expenses:
                print("No expenses yet.")
            else:
                total = 0
                print("\nYour Expenses:")
                for idx, expense in enumerate(expenses, start=1):
                    print(f"{idx}. {expense['name']} - ₱{expense['amount']}")
                    total += expense['amount']
                print(f"\nTotal: ₱{total}")

        # Adding The Expense
        elif choice == "2":
            name = input("Enter your expense name: ")
            amount = float(input("Enter The amount: ₱"))
            expenses.append({"name": name, "amount": amount})
            print(f"Expense added successfully: {name} - ₱{amount}")

        # Update The Expense
        elif choice == "3":
            if not expenses:
                print("No expenses to update.")
            else:
                print("\nSelect an expense to update:")
                for idx, expense in enumerate(expenses, start=1):
                    print(f"{idx}. {expense['name']} - ₱{expense['amount']}")
                try:
                    exp_index = int(input("Enter the number of the expense to update: ")) - 1
                    if 0 <= exp_index < len(expenses):
                        new_name = input("Enter new expense name: ")
                        new_amount = float(input("Enter new amount: ₱"))
                        expenses[exp_index] = {"name": new_name, "amount": new_amount}
                        print(" Expense updated successfully.")
                    else:
                        print(" Invalid expense number.")
                except ValueError:
                    print(" Please enter a valid number.")

        # Removing a Expense
        elif choice == "4":
            if not expenses:
                print("No expenses to remove.")
            else:
                print("\nSelect an expense to remove:")
                for idx, expense in enumerate(expenses, start=1):
                    print(f"{idx}. {expense['name']} - ₱{expense['amount']}")
                try:
                    exp_index = int(input("Enter the number of the expense to remove: ")) - 1
                    if 0 <= exp_index < len(expenses):
                        removed_expense = expenses.pop(exp_index)
                        print(f" Expense '{removed_expense['name']}' removed successfully.")
                    else:
                        print(" Invalid expense number.")
                except ValueError:
                    print("Please enter a valid number.")

        # Exiting The Program
        elif choice == "5":
            print("Exiting program. Goodbye! , Thank You!")
            break

        # Invalid Choices
        else:
            print(" Invalid choice! Please enter a number between 1 and 5.")

main()
