class Book:

    def __init__(self, id_, name, pages):

        self.id = id_

        self.name = name

        self.pages = pages

    def __str__(self):

        return f'Книга "{self.name}"'

    def __repr__(self):

        return f"Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})"

class Library:

    def __init__(self, books=None):

        self.books = books if books is not None else []

    def get_next_book_id(self):

        if not self.books:

            return 1

        else:

            # Получаем ID последней книги и увеличиваем его на 1

            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):

        for index, book in enumerate(self.books):

            if book.id == book_id:

                return index

        # Если цикл завершился, а книга не найдена, вызываем исключение

        raise ValueError("Книги с запрашиваемым id не существует")

# Данные для примера

BOOKS_DATABASE = [

    {

        "id": 1,

        "name": "test_name_1",

        "pages": 200,

    },

    {

        "id": 2,

        "name": "test_name_2",

        "pages": 400,

    }

]

if __name__ == '__main__':

    # Инициализация пустой библиотеки

    empty_library = Library()

    print(f"Следующий ID для пустой библиотеки: {empty_library.get_next_book_id()}")

    # Создаем список объектов Book из словарей

    list_books = [

        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])

        for book_dict in BOOKS_DATABASE

    ]

    # Инициализация библиотеки с книгами

    library_with_books = Library(books=list_books)

    print(f"Следующий ID для библиотеки с книгами: {library_with_books.get_next_book_id()}")

    # Проверка получения индекса книги по ID

    try:

        index_of_book_1 = library_with_books.get_index_by_book_id(1)

        print(f"Индекс книги с ID 1: {index_of_book_1}")

        # Проверка случая, когда книга не существует

        print(library_with_books.get_index_by_book_id(3))

    except ValueError as e:

        print(f"Ошибка: {e}")

