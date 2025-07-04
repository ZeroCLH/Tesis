class Book:
    def __init__(self, categoryId, author, publisher, publication_year, isbn, type, cover, description, photo):
        self.categoryId = categoryId
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.isbn = isbn
        self.type = type
        self.cover = cover
        self.description = description
        self.photo = photo  

    
    def getBook(self):
        return self.__dict__