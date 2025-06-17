from datetime import datetime

class User:

    def __init__(self, identification, name, password, rol, state):
        self.identification = identification
        self.name = name
        self.password = password
        self.rol = rol
        self.state = state
    
    def getUser(self):
        return self.__dict__
    
    def createUser(self):
        self.creationDate = datetime.now()

    def updateUser(self):
        self.updateDate = datetime.now()