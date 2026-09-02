"""
Optional text-based console interface.

This is NOT required to run the system (use main.py / gui.py for the
graphical version), but it demonstrates that the same model layer
(library.py, member.py, ...) can power more than one interface, since
none of those classes read from input() or print() themselves anymore.
"""

from library import Library
from member import Member
from librarian import Librarian


def main():
    library = Library("Alexandria Library", max_items=20)

    member = Member(1, "Mahmoud", "mahmoud@gmail.com", 101)
    librarian = Librarian(2, "Ahmed", "ahmed@gmail.com", 501)

    library.add_member(member)
    library.add_librarian(librarian)

    while True:
        print("\n================================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Delete a Book")
        print("6. Edit Book Details")
        print("7. View All Books")
        print("8. View My Borrowed Books")
        print("9. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                title = input("Enter book title: ")
                description = input("Enter description: ")
                author = input("Enter author: ")
                book = library.add_book(title, description, author)
                print(f"Book added successfully! (ID: {book.item_id})")

            elif choice == "2":
                query = input("Enter book title to search: ")
                results = library.search_items(query)
                if not results:
                    print("Book not found.")
                for item in results:
                    print("\n" + item.get_info())

            elif choice == "3":
                book_id = int(input("Enter book ID to issue: "))
                loan = library.issue_item(member, book_id)
                print(f"'{loan.item.title}' issued to {member.name}. Due: {loan.due_date}")

            elif choice == "4":
                book_id = int(input("Enter book ID to return: "))
                library.return_item(member, book_id)
                print("Book returned successfully.")

            elif choice == "5":
                book_id = int(input("Enter book ID to delete: "))
                library.delete_item(book_id)
                print("Book deleted successfully.")

            elif choice == "6":
                book_id = int(input("Enter book ID to edit: "))
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                library.edit_item(book_id, title=new_title, description=new_description)
                print("Book details updated successfully!")

            elif choice == "7":
                items = library.view_all_items()
                if not items:
                    print("No books available.")
                for item in items:
                    print("------------------------")
                    print(item.get_info())

            elif choice == "8":
                borrowed = member.get_borrowed_books()
                if not borrowed:
                    print("No borrowed books.")
                for book in borrowed:
                    print(f"ID: {book.item_id} - {book.title}")

            elif choice == "9":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
