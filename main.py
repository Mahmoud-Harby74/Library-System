"""
Entry point for the Library Management System.

Running this file launches the desktop GUI (gui.py), which is built on
top of the same model classes (Library, Member, Librarian, Book,
Magazine, Loan, ...).

The original text-based console menu is still available in
main_console.py if you ever want to run the system without a GUI.
"""

from gui import LibraryApp


def main():
    app = LibraryApp()
    app.mainloop()


if __name__ == "__main__":
    main()
