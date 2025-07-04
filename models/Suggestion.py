from datetime import datetime
class Suggestion:
    
    def __init__(self, userId, seggestedTitle, seggestedAuthor, reason, date):    
        self.userId = userId
        self.seggestedTitle = seggestedTitle
        self.seggestedAuthor = seggestedAuthor
        self.reason = reason
        

       
    def getSuggestion(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()