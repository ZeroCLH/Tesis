from datetime import datetime
class History:
    
    def __init__(self, userId, bookId, readingDate):    
        self.userId = userId
        self.bookId = bookId    
        
        
    def getHisory(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()