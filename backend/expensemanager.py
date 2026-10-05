from expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses=[]
        self.next_id=1

    def add_expense(self,title,amount,category,date):
        expense=Expense(self.next_id,title,amount,category,date)
        self.expenses.append(expense)
        self.next_id += 1
        return expense

    def delete_expense(self,id):
        self.expenses=[expense for expense in self.expenses if expense.id != id]

    def list_expenses(self):
        return self.expenses
        
    def get_total(self):
        return sum(e.amount for e in self.expenses)

    def filter_by_category(self,category):
        return [expense for expense in self.expenses if expense.category == category]

    