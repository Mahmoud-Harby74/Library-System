class Library:
    def __init__(self, name, max_books=20):
        self.__name = name
        self.__max_books = max_books

        self.__items = []
        self.__members = []
        self.__librarians = []

    @property
    def name(self):
        return self.__name

    def add_book(self):
        if len(self.__items) >= self.__max_books:
            print("Maximum book limit reached.")
            return

        print("\n=== Add Book ===")

        title = input("Enter book title: ")
        description = input("Enter description: ")
        author = input("Enter author: ")

        item_id = len(self.__items) + 1

        from book import Book

        book = Book(
            item_id,
            title,
            description,
            author
        )

        self.__items.append(book)

        print("Book added successfully!")

    def search_book(self):
        print("\n=== Search Book ===")

        title = input("Enter book title to search: ")

        found = False

        for item in self.__items:
            if item.title.lower() == title.lower():

                print("\nBook found!")
                print(item.get_info())

                found = True

        if not found:
            print("Book not found.")

    def issue_book(self, member):
        print("\n=== Issue Book ===")

        try:
            book_id = int(input("Enter book ID to issue: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if book_id <= 0 or book_id > len(self.__items):
            print("Invalid book ID.")
            return

        book = self.__items[book_id - 1]

        if member.borrow_book(book):
            print(f"Book '{book.title}' issued to {member.name}.")

    def return_book(self, member):
        print("\n=== Return Book ===")

        try:
            book_id = int(input("Enter book ID to return: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if book_id <= 0 or book_id > len(self.__items):
            print("Invalid book ID.")
            return

        book = self.__items[book_id - 1]

        member.return_book(book)

    def delete_book(self):
        print("\n=== Delete Book ===")

        try:
            book_id = int(input("Enter book ID to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if book_id <= 0 or book_id > len(self.__items):
            print("Invalid book ID.")
            return

        book = self.__items[book_id - 1]

        if not book.is_available:
            print("Cannot delete an issued book.")
            return

        self.__items.pop(book_id - 1)

        # Re-number IDs
        for i, item in enumerate(self.__items):
            item._Item__item_id = i + 1

        print("Book deleted successfully.")

    def edit_book(self):
        print("\n=== Edit Book ===")

        try:
            book_id = int(input("Enter book ID to edit: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if book_id <= 0 or book_id > len(self.__items):
            print("Invalid book ID.")
            return

        book = self.__items[book_id - 1]

        new_title = input("Enter new title: ")
        new_description = input("Enter new description: ")

        book.title = new_title
        book.description = new_description

        print("Book details updated successfully!")

    def view_all_books(self):
        print("\n=== All Books ===")

        if not self.__items:
            print("No books available.")
            return

        for item in self.__items:
            print("------------------------")
            print(item.get_info())

    def add_member(self, member):
        self.__members.append(member)

    def add_librarian(self, librarian):
        self.__librarians.append(librarian)