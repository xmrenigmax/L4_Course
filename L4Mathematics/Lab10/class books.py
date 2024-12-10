class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")  # Debug statement

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed")
                else:
                    print("Book not available")
                return 
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned")
                else:
                    print("Book already available")
                return 
        print("Book not found") 

    def display_info(self):
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("Is available:", book.is_available)


library = Library()
book1 = Book("Harry Potter", "J.K. Rowling", True)
book2 = Book("The Hobbit", "J.R.R. Tolkien", False)

library.add_book(book1)
library.add_book(book2)

print("Library inventory after adding books:")
library.display_info()

library.borrow_book("Harry Potter")
print("\nLibrary inventory after borrowing 'Harry Potter':")
library.display_info()

library.return_book("Harry Potter")
print("\nLibrary inventory after returning 'Harry Potter':")
library.display_info()