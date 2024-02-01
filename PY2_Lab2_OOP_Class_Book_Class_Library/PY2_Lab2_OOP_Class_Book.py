BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация, создание экземпляра класса Book (книга).

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """

        # Проверяем, что полученная о книге информация корректна
        self.check_book_input_data(id_, name, pages)

        self.id_ = id_
        self.name = name
        self.pages = pages

    def check_book_input_data(self, id_: int, name: str, pages: int):
        """
        Внутренний вспомогательный метод для проверки, что полученная о книге информация корректна

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        :raise TypeError: Идентификатор книги и Количество страниц в книге должны быть типа int, Название книги - типа str
        :raise ValueError: Идентификатор книги должен быть >= 1
                           Название книги должно быть как минимум из 1 символа
                           Количество страниц в книге должно быть >= 1
        """

        # Проверяем типы данных
        if not (isinstance(id_, int) and isinstance(name, str) and isinstance(pages, int)):
            raise TypeError(
                "Идентификатор книги и Количество страниц в книге должны быть типа int, Название книги - типа str")

        # Проверяем значения переменных
        if not (id_ >= 1 and len(name) >= 1 and pages >= 1):
            raise ValueError("Идентификатор книги должен быть >= 1 \
                              Название книги должно быть как минимум из 1 символа \
                              Количество страниц в книге должно быть >= 1")

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__