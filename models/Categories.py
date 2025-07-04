from datetime import datetime
class Categories:
    
    def __init__(self, name, description):    
        self.name = name
        self.description = description

       
    def getCategories(self):
        return self.__dict__

    def returnDate(self):
        self.returnDate = datetime.now()