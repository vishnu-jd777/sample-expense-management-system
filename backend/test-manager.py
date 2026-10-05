from expensemanager import ExpenseManager


manager = ExpenseManager()

manager.add_expense('lunch',400,'food','2023-10-01')
manager.add_expense('dinner',400,'food','2023-10-01')
manager.add_expense('movie',500,'other','2023-10-01')

print("All expenses:")
for e in manager.list_expenses():
    print(e)

print("\nTotal expenses:", manager.get_total())

print("\nExpenses in 'food' category:")
for e in manager.filter_by_category('food'):
    print(e)

manager.delete_expense(2)
print("\nAll expenses after deleting expense with ID 2:")
for e in manager.list_expenses():
    print(e)

manager.add_expense('breakfast',200,'food','2023-10-02')
print("\nAll expenses after adding a new expense:")
for e in manager.list_expenses():
    print(e)