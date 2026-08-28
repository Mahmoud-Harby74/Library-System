from user import User


class Librarian(User):
    def __init__(self, user_id, name, email, employee_id):
        super().__init__(user_id, name, email)

        self.__employee_id = employee_id

    @property
    def employee_id(self):
        return self.__employee_id

    def get_info(self):
        return (
            f"Librarian ID: {self.__employee_id}, "
            f"Name: {self.name}, Email: {self.email}"
        )