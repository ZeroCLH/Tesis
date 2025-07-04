from datetime import datetime
class Favorite:
    
    def __init__(self, userId, bookId, addedDate):
        self.userId = userId
        self.bookId = bookId    
        
        
    def getFavorite(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()