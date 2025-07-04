from datetime import datetime
class Comment:
    
    def __init__(self, userId, bookId, content):    
        self.userId = userId
        self.bookId = bookId    
        self.content = content
        
    def getComment(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()