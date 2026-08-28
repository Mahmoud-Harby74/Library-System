from datetime import date, timedelta


class Loan:
    def __init__(self, loan_id, member, item, loan_days=14):
        self.__loan_id = loan_id
        self.__member = member
        self.__item = item
        self.__borrow_date = date.today()
        self.__due_date = self.__borrow_date + timedelta(days=loan_days)
        self.__return_date = None

    @property
    def loan_id(self):
        return self.__loan_id

    @property
    def member(self):
        return self.__member

    @property
    def item(self):
        return self.__item

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def return_date(self):
        return self.__return_date

    def close_loan(self):
        self.__return_date = date.today()

    def is_overdue(self):
        if self.__return_date is not None:
            return False

        return date.today() > self.__due_date

    def get_loan_info(self):
        return (
            f"Loan ID: {self.__loan_id}\n"
            f"Member: {self.__member.name}\n"
            f"Item: {self.__item.title}\n"
            f"Borrow Date: {self.__borrow_date}\n"
            f"Due Date: {self.__due_date}\n"
            f"Return Date: {self.__return_date}"
        )