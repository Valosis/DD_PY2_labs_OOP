import doctest


class Monitor:
    def __init__(self, manufacturer: str, width_resolution: int, height_resolution: int):
        """
        Инициализация, создание экземпляра класса Monitor (монитор).

        :param manufacturer: Производитель
        :param width_resolution: Разрешение экрана по горизонтали
        :param height_resolution: Разрешение экрана по вертикали

        Примеры:

        >>> monitor_1 = Monitor("Acer", 1920, 1080)
        >>> monitor_2 = Monitor("LG", 3840, 2160)
        """

        # Проверяем, что полученная о мониторе информация корректна
        self.check_monitor_input_data(manufacturer, width_resolution, height_resolution)

        self.manufacturer = manufacturer
        self.width_resolution = width_resolution
        self.height_resolution = height_resolution

        # Калибровка монитора. Считаем, что калибровка задается трехмерным массивом посубпиксельно.
        # По умолчанию все значения 0, так как изначально неизвестны реальные отклонения от правильного цвета каждого из RGB субпикселей.
        # [0, 0, 0] - начальные калибровочные значения для Red, Green, Blue субпикселей
        # Дополнительно смотри метод calibrate_monitor()
        self.monitor_calibration_table = [[[0, 0, 0] for _ in range(self.width_resolution)] for _ in range(self.height_resolution)]

    def check_monitor_input_data(self, manufacturer: str, width_resolution: int, height_resolution: int) -> None:
        """
        Внутренний вспомогательный метод для проверки, что полученная о мониторе информация корректна

        :param manufacturer: Производитель
        :param width_resolution: Разрешение экрана по горизонтали
        :param height_resolution: Разрешение экрана по вертикали
        :raise TypeError: Название manufacturer должно быть типа str, width_resolution и height_resolution только типа int
        :raise ValueError: Название manufacturer должно быть str из хотя бы одного символа,
                            width_resolution и height_resolution должны быть положительные
        :return: None

        Примеры:

        #>>> self.check_monitor_input_data(8373O9, "ABC", 7.55)
        #>>> self.check_monitor_input_data(4.3, 5, "LG")
        #>>> self.check_monitor_input_data("Asus", 0, -500)
        #>>> self.check_monitor_input_data("AOC", 1600, 900)
        """

        # Проверяем типы данных
        if not (isinstance(manufacturer, str) and isinstance(width_resolution, int) and isinstance(height_resolution, int)):
            raise TypeError("Название manufacturer должно быть типа str, width_resolution и height_resolution только типа int")

        # Проверяем значения переменных
        if not (len(manufacturer) > 0 and width_resolution > 0 and height_resolution > 0):
            raise ValueError("Название manufacturer должно быть str из хотя бы одного символа, "
                                "width_resolution и height_resolution должны быть положительные")

    def calibrate_monitor(self, monitor_calibration_table: list) -> None:
        """
        Передаем таблицу monitor_calibration_table со значениями для каждого субпикселя RGB для компенсации отклонения цвета.

        :param monitor_calibration_table: Таблица со значениями для каждого субпикселя RGB для компенсации отклонения цвета.
        :return: None

        Примеры:

        >>> monitor = Monitor("Asus", 5, 2)
        >>> monitor.calibrate_monitor([ [[-1, 5, -3], [2, 10, -7], [-23, 0, 1], [15, -5, 0], [-18, -13, 5]]  , \
                                        [[0, -8, 0], [6, 1, 1], [15, 3, 8], [-3, 3, 16], [-10, -1, 9]] ])
        """

        # Метод для проверки корректной структуры таблицы
        # check_monitor_calibration_table(monitor_calibration_table)
        self.monitor_calibration_table = monitor_calibration_table

    def calculate_gpu_load_difference(self, width_resolution: int, height_resolution: int) -> float:
        """
        Определяет насколько больше или меньше данный монитор по сравнению с другим нагружает видеокарту, например, в играх.
        Зависит от суммарного количества пикселей (отношения количества).
        Например, для 2560x1440 и 1920x1080 коэффициент производительности составляет
        (2560x1440)/(1920x1080) = 16/9 = 1.78

        :param width_resolution: Разрешение экрана по горизонтали
        :param height_resolution: Разрешение экрана по вертикали
        :return: Возвращает коэффициент производительности

        Примеры:
        >>> monitor = Monitor("Asus", 2560, 1440)
        >>> monitor.calculate_gpu_load_difference(1920, 1080)
        1.78
        """

        # Проверяем, что полученная о мониторе информация корректна
        self.check_monitor_input_data("Empty_Name", width_resolution, height_resolution)

        return round((self.width_resolution * self.height_resolution)/(width_resolution * height_resolution), 2)


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
