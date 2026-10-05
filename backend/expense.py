class  Expense:

    def __init__(self,id,title,amount,category,date):
        self.id=id
        self.title=title
        self.amount=amount
        self.category=category
        self.date=date
    def __str__(self):
        return f"{self.id}. {self.title}-₹{self.amount}  [{self.category}] on {self.date}"
