class Library:
    """
    Core library engine.

    Every public method here is GUI-friendly:
    - No input()/print() calls.
    - Success -> returns a value (the item, the loan, a list, etc.)
    - Failure -> raises ValueError with a human-readable message.

    Any interface (console, GUI, tests, ...) can be built on top of it.
    """

    def __init__(self, name, max_items=50):
        self.__name = name
        self.__max_items = max_items

        self.__items = []
        self.__members = []
        self.__librarians = []
        self.__loans = []

    # ---------------------------------------------------------------- info

    @property
    def name(self):
        return self.__name

    @property
    def items(self):
        return list(self.__items)

    @property
    def members(self):
        return list(self.__members)

    @property
    def librarians(self):
        return list(self.__librarians)

    @property
    def loans(self):
        return list(self.__loans)

    # --------------------------------------------------------------- items

    def _next_item_id(self):
        return len(self.__items) + 1

    def add_book(self, title, description, author):
        self._check_capacity()
        title = self._require_text(title, "Title")
        author = self._require_text(author, "Author")
        description = (description or "").strip()

        from book import Book

        book = Book(self._next_item_id(), title, description, author)
        self.__items.append(book)

        return book

    def add_magazine(self, title, description, issue_number):
        self._check_capacity()
        title = self._require_text(title, "Title")
        description = (description or "").strip()

        from magazine import Magazine

        magazine = Magazine(self._next_item_id(), title, description, issue_number)
        self.__items.append(magazine)

        return magazine

    def _check_capacity(self):
        if len(self.__items) >= self.__max_items:
            raise ValueError("Maximum item limit reached for this library.")

    @staticmethod
    def _require_text(value, field_name):
        value = (value or "").strip()
        if not value:
            raise ValueError(f"{field_name} cannot be empty.")
        return value

    def get_item_by_id(self, item_id):
        for item in self.__items:
            if item.item_id == item_id:
                return item
        raise ValueError(f"No item found with ID {item_id}.")

    def search_items(self, query):
        """Case-insensitive search across title, author and description."""
        query = (query or "").strip().lower()

        if not query:
            return list(self.__items)

        results = []
        for item in self.__items:
            haystack = item.title.lower() + " " + item.description.lower()
            if hasattr(item, "author"):
                haystack += " " + item.author.lower()

            if query in haystack:
                results.append(item)

        return results

    def delete_item(self, item_id):
        item = self.get_item_by_id(item_id)

        if not item.is_available:
            raise ValueError("Cannot delete an item that is currently issued.")

        self.__items.remove(item)

        # keep IDs contiguous, same behaviour as the original console version
        for index, remaining in enumerate(self.__items):
            remaining._Item__item_id = index + 1

        return True

    def edit_item(self, item_id, title=None, description=None, author=None,
                  issue_number=None):
        item = self.get_item_by_id(item_id)

        if title is not None:
            item.title = self._require_text(title, "Title")

        if description is not None:
            item.description = description.strip()

        if author is not None and hasattr(item, "author"):
            item.author = self._require_text(author, "Author")

        if issue_number is not None and hasattr(item, "issue_number"):
            item.issue_number = issue_number

        return item

    def view_all_items(self):
        return list(self.__items)

    # -------------------------------------------------- members/librarians

    def add_member(self, member):
        self.__members.append(member)
        return member

    def add_librarian(self, librarian):
        self.__librarians.append(librarian)
        return librarian

    def register_member(self, name, email):
        name = self._require_text(name, "Name")
        email = self._require_text(email, "Email")

        if "@" not in email:
            raise ValueError("Please enter a valid email address.")

        from member import Member

        member_id = len(self.__members) + 1
        user_id = len(self.__members) + len(self.__librarians) + 1

        member = Member(user_id, name, email, member_id)
        self.__members.append(member)

        return member

    # -------------------------------------------------------------- loans

    def issue_item(self, member, item_id, loan_days=14):
        item = self.get_item_by_id(item_id)

        member.borrow_book(item)  # raises ValueError on failure

        from loan import Loan

        loan = Loan(len(self.__loans) + 1, member, item, loan_days)
        self.__loans.append(loan)

        return loan

    def return_item(self, member, item_id):
        item = self.get_item_by_id(item_id)

        member.return_book(item)  # raises ValueError on failure

        for loan in self.__loans:
            if loan.item is item and loan.member is member and loan.return_date is None:
                loan.close_loan()
                return loan

        return None

    def active_loans(self, member=None):
        loans = [loan for loan in self.__loans if loan.return_date is None]

        if member is not None:
            loans = [loan for loan in loans if loan.member is member]

        return loans

    def all_loans(self, member=None):
        loans = list(self.__loans)

        if member is not None:
            loans = [loan for loan in loans if loan.member is member]

        return loans
