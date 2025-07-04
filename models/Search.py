from datetime import datetime
class Search:
    
    def __init__(self, userId, searchesText, date):
        self.userId = userId
        self.searchesText = searchesText
        
    def getSearch(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()