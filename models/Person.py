from datetime import datetime
class Person:
    def __init__(self,identification, lastName, firstName, age, address, email, phone, photo)   
        self.identification = identification
        self.lastName = lastNamename
        self.firstName = firstName
        self.age = age
        self.address = address  
        self.email = email
        self.phone = phone
        self.photo = photo

    def getPerson(self):
        return self.__dict__
    
    def createPerson(self):
        self.creationDate = datetime.now()
    
    def returnDate (self):  
        self.returnDate = datetime.now

    def updatePerson(self):
        self.updateDate = datetime.now()