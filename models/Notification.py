from datetime import datetime
class Notification:
    def __init__(self, userId, message, type, status, date):
        self.userId = userId
        self.message = message
        self.type = type
        self.status = status
    
    def getNotification(self):
        return self.__dict__
    
    def returnDate(self):
        self.returnDate = datetime.now()