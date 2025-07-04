from datetime import datetime
class User:

    def __init__(self, personID, username, password, status, rol):
        self.personID = personID
        self.username = username
        self.password = password
        self.state = state
        self.rol = rol
        
    
    def getUser(self):
        return self.__dict__
    
    def createUser(self):
        self.creationDate = datetime.now()

    def updateUser(self):
        self.updateDate = datetime.now()