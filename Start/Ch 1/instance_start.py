# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret message'

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price
    
    def setDiscount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("Sherlock Holmes", 'Sir Arthur Conan Doyle', 600, 34.99)
b2 = Book("The Lord of The Rings", 'John Ronald Reuel Tolkien', 1500, 59.99)

# TODO: print the price of book1
print(b1.getPrice())

# TODO: try setting the discount
print(b2.getPrice())
b2.setDiscount(0.10)
print(b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)