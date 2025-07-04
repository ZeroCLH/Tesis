from datetime import datetime
class Reservation:
    
    def __init__(self, userId, bookId, reservationDate, status):
        self.userId = userId
        self.bookId = bookId
        self.status = status
        
    def getReservation(self):
        return self.__dict__

    def createReservation(self):    
        self.creationDate = datetime.now()

    def returnDate(self):
        self.returnDate = datetime.now()