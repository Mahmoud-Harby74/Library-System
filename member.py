from user import User


class Member(User):
    MAX_BORROWED_ITEMS = 3

    def __init__(self, user_id, name, email, member_id):
        super().__init__(user_id, name, email)

        self.__member_id = member_id
        self.__borrowed_books = []

    @property
    def member_id(self):
        return self.__member_id

    @property
    def borrowed_books(self):
        return list(self.__borrowed_books)

    def borrow_book(self, book):
        if not book.is_available:
            raise ValueError(f"'{book.title}' is already issued to someone else.")

        if len(self.__borrowed_books) >= self.MAX_BORROWED_ITEMS:
            raise ValueError(
                f"{self.name} cannot borrow more than "
                f"{self.MAX_BORROWED_ITEMS} items at a time."
            )

        self.__borrowed_books.append(book)
        book.is_available = False

        return True

    def return_book(self, book):
        if book not in self.__borrowed_books:
            raise ValueError(f"'{book.title}' was not borrowed by {self.name}.")

        self.__borrowed_books.remove(book)
        book.is_available = True

        return True

    def get_borrowed_books(self):
        return list(self.__borrowed_books)

    def get_info(self):
        return (
            f"Member ID: {self.__member_id}, "
            f"Name: {self.name}, Email: {self.email}"
        )
