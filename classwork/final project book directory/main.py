class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reservation_status = False  # Initialize all books as not reserved


class BookReservationSystem:
    def __init__(self):
        self.books = []  # dictionary List used to store books

    def add_book(self, title, author):  # function to add a book
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added successfully.")

    def check_reservation_status(self, title):  # function to check if a book is reserved
        for book in self.books:
            if book.title == title:
                if book.reservation_status:
                    print(f"Book '{title}' is currently reserved.")
                else:
                    print(f"Book '{title}' is available for reservation.")
                return
        print(f"Book '{title}' not found in the system.")  # safeguard for improperly typed books or not available books

    def reserve_book(self, title):  # function used to reserve a book within the book directory
        for book in self.books:
            if book.title == title:
                if not book.reservation_status:
                    book.reservation_status = True
                    print(f"Book '{title}' reserved successfully.")
                else:
                    print(f"Book '{title}' is already reserved.")
                return
        print(f"Book '{title}' not found in the system.")

    def cancel_reservation(self, title):  # a function to cancel a book reservation within the book directory
        for book in self.books:
            if book.title == title:
                if book.reservation_status:
                    book.reservation_status = False
                    print(f"Reservation for book '{title}' cancelled successfully.")
                else:
                    print(f"Book '{title}' is not reserved.")
                return
        print(f"Book '{title}' not found in the system.")

    def display_reserved_books(self):  # a function to display all the currently reserved books in the directory
        reserved_books = [book for book in self.books if book.reservation_status]
        if reserved_books:
            print("Reserved Books:")
            for book in reserved_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books are currently reserved.")


# usage of the above created functions to access the directory
book_system = BookReservationSystem()
book_system.add_book(input("Please enter the title of the book you would like to add:"),
                     input("Please enter the author of the book you would like to add:"))
book_system.check_reservation_status(input("please enter the title of the book to check reservation status:"))
book_system.add_book(input("Please enter the title of the book you would like to add:"),
                     input("Please enter the author of the book you would like to add:"))
book_system.check_reservation_status(input("please enter the title of the book to check reservation status:"))

book_system.reserve_book(input("please enter the title of the book to reserve it:"))
book_system.check_reservation_status(input("please enter the title of the book to check reservation status:"))

book_system.reserve_book(input("please enter the title of the book to reserve it:"))
book_system.check_reservation_status(input("please enter the title of the book to check reservation status:"))

book_system.cancel_reservation(input("please enter the title of the book to cancel reservation status:"))
book_system.check_reservation_status(input("please enter the title of the book to check reservation status:"))

book_system.display_reserved_books()
