# Комментарий к конструктору класса Library

class LibraryGood:
    def __init__(self, books = None):
        if(books is None):
            books = []

        self.books = books


class LibraryBad:
    def __init__(self, books = []):
        self.books = books
        

def test_LibraryGood():
    print("\n\n===Start testing LibraryGood===")

    libraryGood_1 = LibraryGood()
    libraryGood_2 = LibraryGood()
    print("Is libraryGood_1.books the same as libraryGood_2.books?")
    print("Answer  :", libraryGood_1.books is libraryGood_2.books)
    # Answer  : False
    print("Expected: False\n")
    # Expected: False


    libraryGood_1.books.append(1)
    libraryGood_2.books.append(2)
    print("Is libraryGood_1.books the same as libraryGood_2.books?")
    print("Answer  :", "libraryGood_1:", libraryGood_1.books, "libraryGood_2:", libraryGood_2.books)
    # Answer  : libraryGood_1: [1] libraryGood_2: [2]
    print("Expected:", "libraryGood_1: [1] libraryGood_2: [2]")
    # Expected: libraryGood_1: [1] libraryGood_2: [2]



def test_LibraryBad():
    print("\n\n===Start testing LibraryBad===")

    libraryBad_1 = LibraryBad()
    libraryBad_2 = LibraryBad()
    print("Is libraryBad_1.books the same as libraryBad_2.books?")
    print("Answer  :", libraryBad_1.books is libraryBad_2.books)
    # Answer  : True
    print("Expected:", "False\n")
    # Expected: False


    libraryBad_1.books.append(1)
    libraryBad_2.books.append(2)
    print("Is libraryBad_1.books the same as libraryBad_2.books?")
    print("Answer  :", "libraryBad_1:", libraryBad_1.books, "libraryBad_2:", libraryBad_2.books)
    # Answer  : libraryGood_1: [1, 2] libraryGood_2: [1, 2]
    print("Expected:", "libraryBad_1: [1]    libraryBad_2: [2]")
    # Expected: libraryGood_1: [1] libraryGood_2: [2]


if __name__ == "__main__":
    test_LibraryGood()
    test_LibraryBad()

    print()