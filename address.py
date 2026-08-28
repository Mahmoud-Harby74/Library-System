class Address:
    def __init__(self, city, street, building):
        self.__city = city
        self.__street = street
        self.__building = building

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def building(self):
        return self.__building

    def get_address(self):
        return f"{self.__building}, {self.__street}, {self.__city}"