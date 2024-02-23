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


# TODO написать класс Book
# Из файла PY2_Lab2_OOP_Class_Book.py
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



# TODO написать класс Library
class Library:
    """
    Конструктор выглядит не так

    def __init__(self, books = []):
        self.books = books

    поскольку в таком случае при создании двух библиотек со значением по умолчанию (books = [])
    в дальнейшим они будут указывать (ссылаться) на один и тот же список

    P.S. При необходимости см. дополнительный файл PY2_Lab2_OOP_Class_LibraryGood_vs_LibraryBad.py
    """

    def __init__(self, books=None):
        """
            Инициализация, создание экземпляра класса Library (библиотека).

            :param books: Список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книги есть, то возвращается идентификатор последней книги, увеличенный на 1.
        Если книг в библиотеке нет, то возвращается 1.

        :return: возвращается идентификатор для добавления новой книги в библиотеку
        """

        # The time-complexity for len(list):
        # Operation     Average Case    Amortized Worst Case
        # Get Length    O(1)            O(1)
        # https://wiki.python.org/moin/TimeComplexity
        return self.books[-1].id_+1 if len(self.books) >= 1 else 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param id_: Идентификатор книги
        :raise ValueError: Если книга с нужным id отсутствует, то вызываем ошибку
                                ValueError "Книги с запрашиваемым id не существует"
        :return: Возвращается индекс книги в списке
        """

        for i, book in enumerate(self.books):
            if book.id_ == id_:
                # Книга с нужным id найдена, возвращается её индекс в списке
                return i

        # Книга с нужным id отсутствует, вызывается ошибка ValueError
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
