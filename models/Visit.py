from datetime import datetime
class Vist:
    
    def __init__(self, userId, dateTime, action, deviceIP):    
        self.userId = userId
        self.action = action
        self.deviceIP = deviceIP
       
    def getVist(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()