from item import Item


class Magazine(Item):
    def __init__(self, item_id, title, description, issue_number):
        super().__init__(item_id, title, description)

        self.__issue_number = issue_number

    @property
    def issue_number(self):
        return self.__issue_number

    def get_info(self):
        status = "Available" if self.is_available else "Issued"

        return (
            f"ID: {self.item_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Issue Number: {self.__issue_number}\n"
            f"Status: {status}"
        )