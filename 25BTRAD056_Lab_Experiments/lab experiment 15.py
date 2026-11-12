class Book:

    def __init__(self, name):
        self.name = name
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(self.name, "issued successfully")
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print(self.name, "returned successfully")

    def display(self):
        print(self.name, "-",
              "Available" if self.available else "Issued")


b1 = Book("Python")
b2 = Book("Java")

b1.issue()
b1.display()
b1.return_book()
b1.display()
b2.display()
