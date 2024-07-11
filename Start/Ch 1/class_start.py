# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    
    # TODO: create a static method
    def getBooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, bookType):
        if bookType not in Book.BOOK_TYPES:
            raise ValueError(f'{bookType} is not a valid book type!')
        self.title = title


# TODO: access the class attribute
print(f'Book Types: {Book.getBookTypes()}')

# TODO: Create some book instances
b1 = Book('Sherlock Holmes', 'PAPERBACK')
b2 = Book('Batman', 'EBOOK')

# TODO: Use the static method to access a singleton object
allBooks = Book.getBooklist()
print(allBooks)
allBooks.append(b1)
allBooks.append(b2)
print(allBooks)