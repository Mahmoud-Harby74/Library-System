from user import User


class Member(User):
    def __init__(self, user_id, name, email, member_id):
        super().__init__(user_id, name, email)

        self.__member_id = member_id
        self.__borrowed_books = []

    @property
    def member_id(self):
        return self.__member_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if not book.is_available:
            print("Book is already issued.")
            return False

        if len(self.__borrowed_books) >= 3:
            print("You cannot borrow more than 3 books.")
            return False

        self.__borrowed_books.append(book)
        book.is_available = False

        print("Book issued successfully.")
        return True

    def return_book(self, book):
        if book not in self.__borrowed_books:
            print("This book was not borrowed by this member.")
            return False

        self.__borrowed_books.remove(book)
        book.is_available = True

        print("Book returned successfully.")
        return True

    def view_borrowed_books(self):
        if not self.__borrowed_books:
            print("No borrowed books.")
            return

        print("\nBorrowed Books:")
        for book in self.__borrowed_books:
            print(f"ID: {book.item_id} - {book.title}")