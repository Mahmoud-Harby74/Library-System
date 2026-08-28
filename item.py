from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, item_id, title, description):
        self.__item_id = item_id
        self.__title = title
        self.__description = description
        self.__is_available = True

    @property
    def item_id(self):
        return self.__item_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value.strip():
            self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, value):
        self.__is_available = value

    @abstractmethod
    def get_info(self):
        pass