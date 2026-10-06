from expensemanager import ExpenseManager


manager = ExpenseManager()


while True:
    print("\n===== EXPENSE MANAGER =====")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Delete Expense")
    print("4. Filter by Category")
    print("5. Show Total")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ").strip()
        if not title:
            print("Title cannot be empty.")
            continue
        try:
            
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        
        category = input("Enter category: ")

        if not category:
            print("Category cannot be empty.")
            continue


        date = input("Enter date (YYYY-MM-DD): ")

        if not date:
            print("Date cannot be empty.")
            continue

        expense = manager.add_expense(
            title,
            amount,
            category,
            date
        )

        print(f"Expense added successfully! ID: {expense.id}")

    elif choice == "2":
        expenses = manager.list_expenses()

        if not expenses:
            print("No expenses found.")
        else:
            print("\n===== EXPENSES =====")

            for expense in expenses:
                print(
                    f"ID: {expense.id} | "
                    f"{expense.title} | "
                    f"₹{expense.amount} | "
                    f"{expense.category} | "
                    f"{expense.date}"
                )

    elif choice == "3":
        expense_id = int(input("Enter expense ID to delete: "))

        if expense_id not in [expense.id for expense in manager.list_expenses()]:
            print("Expense ID not found.")
            continue

        manager.delete_expense(expense_id)

        print("Expense deleted successfully!")

    elif choice == "4":
        category = input("Enter category: ")

        expenses = manager.filter_by_category(category)

        if not expenses:
            print("No expenses found in this category.")
        else:
            for expense in expenses:
                print(
                    f"ID: {expense.id} | "
                    f"{expense.title} | "
                    f"₹{expense.amount} | "
                    f"{expense.date}"
                )

    elif choice == "5":
        total = manager.get_total()

        print(f"Total expenses: ₹{total}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")