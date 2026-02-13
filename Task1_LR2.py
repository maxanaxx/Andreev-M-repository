class Book:
    """
    Класс для представления книги с ее атрибутами.
    """
    def __init__(self, id_, name, pages):
        """
            id_ (int): Уникальный идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):

        return f'Книга "{self.name}"'

    def __repr__(self):

        return f"Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})"

# Пример использования класса Book
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
    # Создаем список объектов Book из словарей
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # Проверяем работу метода __str__
    for book in list_books:
        print(book)

    # Проверяем работу метода __repr__
    print(list_books)
