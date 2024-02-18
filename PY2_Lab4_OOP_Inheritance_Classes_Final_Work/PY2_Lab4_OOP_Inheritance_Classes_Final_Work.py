class Home:
    """ Базовый класс Home (жилье, которое может быть любое) """

    def __init__(self, country: str, city: str):
        """
        Инициализация, создание экземпляра класса Home (жилье).

        :param country: Страна
        :param city: Город
        """
        # country - это свойство, проверка валидности значения происходить в его setter
        self.country = country
        # city - это свойство, проверка валидности значения происходить в его setter
        self.city = city

    @property
    def country(self) -> str:
        """
        getter для country
        """
        return self._country
    @country.setter
    def country(self, new_country: str) -> None:
        """
        setter для country

        :param new_country: Страна
        :raise TypeError: Название страны должно быть типа str
        :raise ValueError: Название страны должно состоять хотя бы из одной буквы
        """

        # Проверяем тип данных
        if not (isinstance(new_country, str)):
            raise TypeError("Название страны должно быть типа str")
        # Проверяем значение переменной
        if not (len(new_country) >= 1):
            raise ValueError("Название страны должно состоять хотя бы из одной буквы")

        self._country = new_country


    @property
    def city(self) -> str:
        """
        getter для city
        """
        return self._city
    @city.setter
    def city(self, new_city: str) -> None:
        """
        setter для city

        :param new_city: Город
        :raise TypeError: Название города должно быть типа str
        :raise ValueError: Название города должно состоять хотя бы из одной буквы
        """

        # Проверяем тип данных
        if not (isinstance(new_city, str)):
            raise TypeError("Название города должно быть типа str")
        # Проверяем значение переменной
        if not (len(new_city) >= 1):
            raise ValueError("Название города должно состоять хотя бы из одной буквы")

        self._city = new_city


    def if_country_city_exist(self) -> bool:
        """
        Проверяем, что такая страна и город существует или что в их написании нет ошибки.
        Согласно заданию реализацию методов писать необязательно, но в общем случае подразумевается
                                                                            обращение к базе данных, поиск в ней.
        В случае неудачи происходит вызов ValueError с информацией о потенциальной орфографической ошибке,
                                                                                если имеются близкие варианты.
        Например, "Россияяя" - "Россия", "Рссия" - "Россия", "Рос" - "Россия"

        :raise ValueError: Если город или страна не нашлись,
            то вызываем ValueError с информацией о потенциальной орфографической ошибке, если имеются близкие варианты.
        :return bool: Возвращается значение true/false - нашлись ли данные страна и город в базе данных или нет.

        Данный метод наследуется в дочерних классах, так как проверка реальности значений country и city одинаковая.
        """
        ...

    def calculate_home_price(self, coefficients: list) -> float:
        """
        Рассчитывается рыночная стоимость жилья (дома, квартиры, апартаментов и т.д.),
                                                                                основанная на множестве параметров.
        Согласно заданию реализацию методов писать необязательно, но подразумевается,
                                что по умолчанию рыночная стоимость жилья рассчитывается на основе страны и города.
        Конечно же, такой подход очень неточный, и является просто формулой по умолчанию.
        Именно поэтому этот метод однозначно должен быть переопределен (реализован, дореализован) в дочерних классах.

        :param coefficients: Входные коэффициенты для подсчета рыночной стоимости жилья
        :return: Рыночная стоимость жилья (дома, квартиры, апартаментов и т.д.)
        """
        ...

    def __str__(self):
        return f"Жилье находится в стране {self.country} и городе {self.city}"

    def __repr__(self):
        return f"{self.__class__.__name__}(country={self.country!r}, city={self.city!r})"


class House(Home):
    """ Дочерний класс House (именно дом, а не жилье в общем) """

    def __init__(self, country: str, city: str, number_of_floors: int):
        """
        Инициализация, создание экземпляра класса House (именно дом, а не жилье в общем).

        :param country: Страна
        :param city: Город
        :param number_of_floors: Количество этажей
        """
        """ Обращаемся к конструктору родительского класса, передавая все нужные аргументы,
                                                                      дабы не повторяться и не нарушать принцип DRY."""
        super().__init__(country, city)
        # number_of_floors - это свойство, проверка валидности значения происходить в его setter
        self.number_of_floors = number_of_floors

    @property
    def number_of_floors(self) -> int:
        """
        getter для number_of_floors
        """
        return self._number_of_floors
    @number_of_floors.setter
    def number_of_floors(self, new_number_of_floors: int) -> None:
        """
        setter для number_of_floors

        :param new_number_of_floors: Количество этажей
        :raise TypeError: Количество этажей должно быть типа int
        :raise ValueError: Количество этажей должно быть >= 1
        """

        # Проверяем тип данных
        if not (isinstance(new_number_of_floors, int)):
            raise TypeError("Количество этажей должно быть типа int")
        # Проверяем значение переменной
        if not (new_number_of_floors >= 1):
            raise ValueError("Количество этажей должно быть >= 1")

        self._number_of_floors = new_number_of_floors


    """
    Метод if_country_city_exist() наследуется в дочерних классах, 
                                    так как проверка реальности значений country и city одинаковая.
    P.S. Смотри описание метода в родительском классе.
    """

    def calculate_home_price(self, coefficients: list, current_debts_state: int) -> float:
        """
        Рассчитывается рыночная стоимость жилья (дома, квартиры, апартаментов и т.д.),
        основанная на стране, городе, количестве этажей дома,

        :param coefficients: Входные коэффициенты для подсчета рыночной стоимости жилья
        :param current_debts_state: Наличие задолженностей или недоплат, связанных с прошлыми или текущими владельцами.
                                    Передается самый актуальный статус, полученный из базы данных федерального агенства.
        :return: Рыночная стоимость жилья (дома, квартиры, апартаментов и т.д.)
        """
        ...

    """
    Метод __str__ может быть унаследован классом House, то есть остаться без изменений,
                                                    поскольку вывод общей информации о жилье не отличается.
    def __str__(self):
        return f"Жилье находится в стране {self.country} и городе {self.city}"
    """

    def __repr__(self):
        """
        Метод __repr__ НЕ может быть унаследован классом House, поскольку этот метод
            выдает такое строковое представление объекта, по которому может быть воссоздан сам экземпляр класса.
        self.class.name - действительно является уместным выбором, так как он позволяет
            динамически выводить название класса.
        Однако в случае House мы имеем параметр number_of_floors, которого нет в базовом классе.
        """
        return f"{self.__class__.__name__}(country={self.country!r}, city={self.city!r}, " \
               f"number_of_floors={self.number_of_floors})"


if __name__ == '__main__':
    ...
