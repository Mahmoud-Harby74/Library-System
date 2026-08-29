# Library Management System

## Project Overview

The **Library Management System** is a Python-based application designed to manage books and library members using Object-Oriented Programming (OOP).

The system allows users to add, search, issue, return, edit, and delete books. It also allows members to view the books they have borrowed.

The main goal of this project is to demonstrate the practical use of the main Object-Oriented Programming concepts in Python.

---

## Main Features

The system provides the following functionalities:

* Add a new book.
* Search for a book by title or information.
* Issue/borrow a book.
* Return a borrowed book.
* Delete a book.
* Edit book details.
* View all available books.
* View books borrowed by the current member.
* Validate user input.
* Handle invalid operations and error cases.

---

## OOP Concepts Used

### 1. Encapsulation

Encapsulation is used to protect the internal data of classes.

Private and protected attributes such as `_attribute` and `__attribute` are used where appropriate.

Getters and setters or properties can be used to safely access and modify object data.

For example, book information and member information are kept inside their corresponding classes instead of being directly managed throughout the whole program.

---

### 2. Abstraction

Abstraction is used to define common behavior that subclasses must implement.

The project uses abstract classes with Python's `abc` module and `@abstractmethod` where appropriate.

This allows the system to define general behavior while leaving the specific implementation to subclasses.

---

### 3. Inheritance

Inheritance is used to reuse common attributes and methods between related classes.

Examples of inheritance relationships in the project include:

* `User → Member`
* `User → Librarian`

and/or other related classes depending on the implementation.

This reduces code duplication and allows subclasses to reuse functionality from their parent classes.

---

### 4. Polymorphism

Polymorphism allows different classes to provide their own implementation of the same method.

The project demonstrates **method overriding**, where subclasses redefine inherited methods according to their own behavior.

The project can also use Python-style method overloading through techniques such as default arguments, `*args`, `**kwargs`, or dynamic typing when needed.

---

## Class Relationships

### Association

Association is used when two classes work with each other but neither class completely owns the other.

For example, a `Member` interacts with `Book` objects when borrowing or returning books.

---

### Aggregation

Aggregation is used when one class contains or manages objects of another class, but those objects can exist independently.

For example, the library can manage a collection of books while the individual book objects can conceptually exist independently of the library.

---

### Composition

Composition is used when one object strongly owns another object and the contained object depends on the lifetime of the owner.

The project uses composition where appropriate to represent objects that are created and managed as part of another class.

---

## Main Classes

The project is organized into classes with separate responsibilities.

### User

Represents a general user of the library system and contains common user information and behavior.

### Member

Represents a library member who can borrow and return books.

### Librarian

Represents a librarian who can perform management operations such as adding, deleting, and editing books.

### Book

Represents a book in the library and stores information such as its title and availability.

### Library

Manages the books and library operations.

> The exact class names may vary depending on the final implementation of the project.

---

## Project Structure

A possible project structure is:

```text
Library-System/
│
├── main.py
├── README.md
├── screenshots/
│   ├── menu.png
│   ├── add_book.png
│   ├── search_book.png
│   ├── issue_book.png
│   └── return_book.png
│
└── other project files
```

---

## How to Run

### Requirements

* Python 3.x
* Any Python IDE or code editor such as VS Code or PyCharm.

### Steps

1. Download or clone the repository.
2. Open the project folder.
3. Open a terminal inside the project folder.
4. Run:

```bash
python main.py
```

If `python` does not work on Windows, use:

```bash
py main.py
```

5. Follow the instructions displayed in the console.

---

## Example Operations

When the program starts, the user can choose from the available options:

```text
================================
   LIBRARY MANAGEMENT SYSTEM
================================
1. Add a Book
2. Search for a Book
3. Issue a Book
4. Return a Book
5. Delete a Book
6. Edit Book Details
7. View All Books
8. View My Borrowed Books
9. Exit
```

The user can select an operation by entering its corresponding number.

---

## Input Validation and Error Handling

The system validates user input and handles invalid operations.

Examples include:

* Preventing invalid menu choices.
* Preventing attempts to issue unavailable books.
* Handling attempts to return books that were not borrowed.
* Handling searches for books that do not exist.
* Validating required information when adding or editing books.

This helps make the application more reliable and user-friendly.

---

## Screenshots

Screenshots demonstrating the application running will be added to this section.

### Main Menu

![Main Menu](screenshots/menu.png)

### Add Book

![Add Book](screenshots/add_book.png)

### Search Book

![Search Book](screenshots/search_book.png)

### Issue Book

![Issue Book](screenshots/issue_book.png)

### Return Book

![Return Book](screenshots/return_book.png)

---

## Conclusion

The Library Management System demonstrates how Object-Oriented Programming can be used to build a practical Python application.

The project applies:

* Encapsulation
* Abstraction
* Inheritance
* Polymorphism
* Association
* Aggregation
* Composition

It also provides the main functionality required for managing books and library members while handling invalid inputs and operations.

## Screenshots

### Main Menu
![Main Menu](screenshots/menu.png)

### Add Book
![Add Book](screenshots/add_book.png)

### Search Book
![Search Book](screenshots/search_book.png)

### Issue Book
![Issue Book](screenshots/issue_book.png)