# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


# Child class
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        # Calling parent class method
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# Creating an object of IssuedBook
issued_book1 = IssuedBook(
    "Python Programming",
    "Guido van Rossum",
    "Ramya",
    "2026-02-04"
)

# Display all details
issued_book1.display_issued_book_details()
