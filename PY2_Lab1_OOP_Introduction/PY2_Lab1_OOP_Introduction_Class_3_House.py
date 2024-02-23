import doctest


class House:
    def __init__(self, number_of_floors: int, number_of_rooms: int, area: float):
        """
        Инициализация, создание экземпляра класса House (дом, квартира, апартаменты).

        :param number_of_floors: Количество этажей
        :param number_of_rooms: Количество комнат
        :param area: Общая площадь

        Примеры:

        >>> house_1 = House(3, 7, 131.6)
        >>> house_2 = House(2, 5, 95.1)
        """

        # Проверяем, что полученная о доме информация корректна
        self.check_house_input_data(number_of_floors, number_of_rooms, area)

        self.number_of_floors = number_of_floors
        self.number_of_rooms = number_of_rooms
        self.area = area

    def check_house_input_data(self, number_of_floors: int, number_of_rooms: int, area: float) -> None:
        """
        Внутренний вспомогательный метод для проверки, что полученная о доме информация корректна

        :param number_of_floors: Количество этажей
        :param number_of_rooms: Количество комнат
        :param area: Общая площадь
        :raise TypeError: Количество этажей и Количество комнат должно быть типа int, Площадь - типа float
        :raise ValueError: Количество этажей и Количество комнат должно быть хотя бы 1, Площадь - более 0
        :return: None

        Примеры:

        #>>> self.check_house_input_data(0, 1, 30)
        #>>> self.check_house_input_data(-1, 1, 0)
        """

        # Проверяем типы данных
        if not (isinstance(number_of_floors, int) and isinstance(number_of_rooms, int) and isinstance(area, float)):
            raise TypeError("Количество этажей и Количество комнат должно быть типа int, Площадь - типа float")

        # Проверяем значения переменных
        if not (number_of_floors >= 1 and number_of_rooms >= 1 and area > 0):
            raise ValueError("Количество этажей и Количество комнат должно быть хотя бы 1, Площадь - более 0")

    def update_house_parameters(self, number_of_floors_new: int, number_of_rooms_new: int, area_new: float) -> None:
        """
        Обновляем информацию о доме в случае, например, пристройки.

        :param number_of_floors_new: Новое количество этажей
        :param number_of_rooms_new: Новое количество комнат
        :param area_new: Новая общая площадь
        :return: None

        Примеры:

        >>> house = House(3, 7, 131.6)
        >>> house.update_house_parameters(3, 9, 160.3)
        """

        # Проверяем, что новая полученная о доме информация корректна
        self.check_house_input_data(number_of_floors_new, number_of_rooms_new, area_new)
        # Проверка, что новые значения >= предыдущих необязательна, так как размеры и правда могли физически уменьшиться

        self.number_of_floors = number_of_floors_new
        self.number_of_rooms = number_of_rooms_new
        self.area = area_new

    def calculate_house_price(self, square_metre_price: float, location_multiplier: float, condition_multiplier: float) -> float:
        """
        Рассчитывает рыночную стоимость дома, квартиры, апартаментов

        :param square_metre_price: Стоимость одного квадратного метра
        :param location_multiplier: Повышающий или понижающий множитель (коэффициент), основанный на местонахождении дома
        :param condition_multiplier: Повышающий или понижающий множитель (коэффициент), основанный на состоянии дома (например, аварийное)
        :return: Рыночная стоимость дома, квартиры, апартаментов

        Примеры:

        >>> house = House(3, 7, 131.6)
        >>> house.calculate_house_price(70000, 0.911, 1.05)
        """

        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
