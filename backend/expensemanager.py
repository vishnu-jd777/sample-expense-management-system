import os
import json
from expense import Expense

class ExpenseManager:
    def __init__(self,filename='expenses.json'):
        self.filename = filename
        self.expenses=[]
        self.next_id=1
        self.load()


    def add_expense(self,title,amount,category,date):
        expense=Expense(self.next_id,title,amount,category,date)
        self.expenses.append(expense)
        self.next_id += 1
        self.save()
        return expense

    def delete_expense(self,id):
        self.expenses=[expense for expense in self.expenses if expense.id != id]
        self.save()

    def list_expenses(self):
        return self.expenses
        
    def get_total(self):
        return sum(e.amount for e in self.expenses)

    def filter_by_category(self,category):
        return [expense for expense in self.expenses if expense.category == category]

    def save(self):
        data=[expense.to_dict() for expense in self.expenses]
        with open(self.filename,'w') as f:
            json.dump(data,f,indent=2)

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename,'r') as file:
            data=json.load(file)
        self.expenses=[Expense.from_dict(item) for item in data]

        if self.expenses:
            self.next_id=max(expense.id for expense in self.expenses)+1


            

    