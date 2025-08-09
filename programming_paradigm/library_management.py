class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                return book.return_book()
        return False

    def list_available_books(self):
        available = []
        for book in self.books:
            if not book.is_checked_out:
                available.append(book)
        return available