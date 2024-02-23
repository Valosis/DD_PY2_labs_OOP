class Book:
    """ Базовый класс Book (книга) """

    def __init__(self, name: str, author: str):
        """
        Инициализация, создание экземпляра класса Book (книга).

        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Атрибут name изменяться не может, поэтому используется НЕ публичный атрибут, а скрытый атрибут (_name),
            для которого реализуется свойство для его получения (getter),
                которое позволяет использовать атрибут только в режиме чтения.
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Атрибут author изменяться не может, поэтому используется НЕ публичный атрибут, а скрытый атрибут (_author),
            для которого реализуется свойство для его получения (getter),
                которое позволяет использовать атрибут только в режиме чтения.
        """
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс PaperBook (бумажная книга) для класса Book (книга)"""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация, создание экземпляра класса PaperBook (бумажная книга).

        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц книги
        """

        """ Обращаемся к конструктору родительского класса, передавая все нужные аргументы,
                                                               дабы не повторяться и не нарушать принцип DRY."""
        super().__init__(name, author)
        # pages - это свойство, проверка валидности значения происходить в его setter
        self.pages = pages

    @property
    def pages(self) -> int:
        """
        getter для pages
        """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """
        setter для pages

        :param new_pages: Количество страниц в книге
        :raise TypeError: Количество страниц в книге должно быть типа int
        :raise ValueError: Количество страниц в книге должно быть >= 1
        """

        # Проверяем тип данных
        if not (isinstance(new_pages, int)):
            raise TypeError(
                "Количество страниц в книге должно быть типа int")
        # Проверяем значение переменной
        if not (new_pages >= 1):
            raise ValueError("Количество страниц в книге должно быть >= 1")

        self._pages = new_pages


    """
    Метод __str__ может быть унаследован классами PaperBook и AudioBook, то есть остаться без изменений,
        поскольку Книга и Автор есть у любой книги, и вывод информации о них не отличается.
        
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"
    """

    def __repr__(self) -> str:
        """
        Метод __repr__ НЕ может быть унаследован классами PaperBook и AudioBook, поскольку этот метод
            выдает такое строковое представление объекта, по которому может быть воссоздан сам экземпляр класса.
        self.class.name - действительно является уместным выбором, так как он позволяет
            динамически выводить название класса.
        Однако в случае PaperBook мы имеем параметр pages, а в случае AudioBook duration, поэтому
            метод __repr__ нужно переопределить.
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс AudioBook (аудиокнига) для класса Book (книга)"""

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация, создание экземпляра класса AudioBook (аудиокнига).

        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность аудиокниги
        """

        """ Обращаемся к конструктору родительского класса, передавая все нужные аргументы,
                                                             дабы не повторяться и не нарушать принцип DRY."""
        super().__init__(name, author)
        # duration - это свойство, проверка валидности значения происходить в его setter
        self.duration = duration

    @property
    def duration(self) -> float:
        """
        getter для duration
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """
        setter для duration

        :param new_duration: Продолжительность аудиокниги
        :raise TypeError: Продолжительность аудиокниги должна быть типа float
        :raise ValueError: Продолжительность аудиокниги должна быть > 0
        """

        # Проверяем тип данных
        if not (isinstance(new_duration, float)):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        # Проверяем значение переменной
        if not (new_duration >= 0):
            raise ValueError("Продолжительность аудиокниги должна быть > 0")

        self._duration = new_duration

    """
    Метод __str__ может быть унаследован классами PaperBook и AudioBook, то есть остаться без изменений,
        поскольку Книга и Автор есть у любой книги, и вывод информации о них не отличается.
        
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"
    """

    def __repr__(self) -> str:
        """
        Метод __repr__ НЕ может быть унаследован классами PaperBook и AudioBook, поскольку этот метод
            выдает такое строковое представление объекта, по которому может быть воссоздан сам экземпляр класса.
        self.class.name - действительно является уместным выбором, так как он позволяет
            динамически выводить название класса.
        Однако в случае PaperBook мы имеем параметр pages, а в случае AudioBook duration, поэтому
            метод __repr__ нужно переопределить.
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.duration!r})"

if __name__ == '__main__':
    ...