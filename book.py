from item import Item


class Book(Item):
    def __init__(self, item_id, title, description, author):
        super().__init__(item_id, title, description)

        self.__author = author

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    def get_info(self):
        status = "Available" if self.is_available else "Issued"

        return (
            f"ID: {self.item_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Author: {self.__author}\n"
            f"Status: {status}"
        )