from expensemanager import ExpenseManager

manager = ExpenseManager()
manager.add_expense("Chai", 20, "food", "2026-10-12")
print("Expenses stored:", len(manager.list_expenses()))