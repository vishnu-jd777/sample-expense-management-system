class  Expense:

    def __init__(self,id,title,amount,category,date):
        self.id=id
        self.title=title
        self.amount=amount
        self.category=category
        self.date=date
    def __str__(self):
        return f"{self.id}. {self.title}-₹{self.amount}  [{self.category}] on {self.date}"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(data['id'], data['title'], data['amount'], data['category'], data['date'])
