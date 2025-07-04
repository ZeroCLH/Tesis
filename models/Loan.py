from datetime import datetime
class Loan:
    
    def __init__(self, userId, bookId, loanDate, returnDate, status):    
        self.userId = userId
        self.bookId = bookId    
        self.status = status
        
    def getloan(self):
        return self.__dict__

    def loanDate(self): 
        self.loanDate = datetime.now

    def returnDate(self):
        self.returnDate = datetime.now()