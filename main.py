from library import Library
from member import Member
from librarian import Librarian


def main():

    # Create Library
    library = Library("Alexandria Library", 20)

    # Create Member
    member = Member(
        1,
        "Mahmoud",
        "mahmoud@gmail.com",
        101
    )

    # Create Librarian
    librarian = Librarian(
        2,
        "Ahmed",
        "ahmed@gmail.com",
        501
    )

    # Add users to library
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

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.search_book()

        elif choice == "3":
            library.issue_book(member)

        elif choice == "4":
            library.return_book(member)

        elif choice == "5":
            library.delete_book()

        elif choice == "6":
            library.edit_book()

        elif choice == "7":
            library.view_all_books()

        elif choice == "8":
            member.view_borrowed_books()

        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()