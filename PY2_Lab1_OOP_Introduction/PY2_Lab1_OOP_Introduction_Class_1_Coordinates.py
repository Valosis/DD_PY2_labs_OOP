import doctest
from typing import Union


class Point:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        """
        Инициализация, создание экземпляра класса Point (точка) с её координатами.
        Используется прямоугольная (декартова) система координат.

        :param x: Абсцисса точки
        :param y: Ордината точки

        Примеры:

        >>> point_1 = Point(-5.55, 8)
        >>> point_2 = Point(3, 834)
        """

        # Проверяем, что полученные координаты являются объектами типа int или float.
        self.check_coordinates_type(x, y)

        self.x = x
        self.y = y

    def check_coordinates_type(self, x_check: Union[int, float], y_check: Union[int, float]) -> None:
        """
        Внутренний вспомогательный метод для проверки, что переданные координаты - это объекты типа int или float.

        :param x_check: Абсцисса точки
        :param y_check: Ордината точки
        :raise TypeError: Если переданные координаты не типа int или float, то вызываем ошибку TypeError
        :return: None

        Примеры:

        #>>> self.check_coordinates_type(5.0, 9)
        #>>> self.check_coordinates_type("5.0", 9)
        #>>> self.check_coordinates_type(5, 9)
        """

        if not (isinstance(x_check, (int, float)) and isinstance(y_check, (int, float))):
            raise TypeError("Обе координаты должны быть типа int или float")

    def update_coordinates(self, x_new: Union[int, float], y_new: Union[int, float]) -> None:
        """
        Обновляем координаты точки.

        :param x_new: Новая абсцисса точки
        :param y_new: Новая ордината точки
        :return: None

        Примеры:

        >>> point = Point(-5.55, 8)
        >>> point.update_coordinates(20, 30)
        """

        # Проверяем, что новые координаты являются объектами типа int или float.
        self.check_coordinates_type(x_new, y_new)
        self.x = x_new
        self.y = y_new

    def to_polar_coordinates(self) -> tuple:
        """
        Преобразовывает (выводит) декартовы координаты в полярные.

        :return: Представление координат точки в полярных координатах

        Примеры:
        >>> point = Point(3, 4)
        >>> point.to_polar_coordinates()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
