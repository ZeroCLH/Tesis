class Resources:
    def __init__(self, bookId, type, url, description):
        self.bookId = bookId
        self.type = type
        self.url = url
        self.description = description
    
    def getResource(self):
        return self.__dict__