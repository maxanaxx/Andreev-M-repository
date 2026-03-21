import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги (не должно быть пустым)
        :param author: Автор книги (не должно быть пустым)
        :param pages: Количество страниц (должно быть положительным целым числом)
        :raises ValueError: Если title или author пустые, pages <= 0 или pages не целое число

        Примеры:
        >>> book = Book("Война и мир", "Л.Н. Толстой", 1225)
        >>> book.title
        'Война и мир'
        >>> book.author
        'Л.Н. Толстой'
        >>> book.pages
        1225
        """
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author
        if not isinstance(pages, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def read_page(self, page_number: int) -> str:
        """
        Прочитать указанную страницу книги.

        :param page_number: Номер страницы для чтения
        :return: Содержимое страницы (заглушка)
        :raises ValueError: Если номер страницы вне допустимого диапазона

        Примеры:
        >>> book = Book("Мастер и Маргарита", "М. Булгаков", 480)
        >>> book.read_page(1)
        'Содержимое страницы 1'
        >>> book.read_page(480)
        'Содержимое страницы 480'
        """
        if page_number < 1 or page_number > self.pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.pages}")
        return f"Содержимое страницы {page_number}"

    def get_book_info(self) -> dict:
        """
        Получить информацию о книге.

        :return: Словарь с информацией о книге

        Примеры:
        >>> book = Book("Преступление и наказание", "Ф. Достоевский", 672)
        >>> book.get_book_info()
        {'title': 'Преступление и наказание', 'author': 'Ф. Достоевский', 'pages': 672}
        """
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages
        }


class Smartphone:
    def __init__(self, brand: str, model: str, battery_level: int = 100):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_level: Уровень заряда батареи (0-100%)
        :raises ValueError: Если уровень заряда вне диапазона 0-100

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 80)
        >>> phone.brand
        'Apple'
        >>> phone.model
        'iPhone 15'
        >>> phone.battery_level
        80
        """
        if not 0 <= battery_level <= 100:
            raise ValueError("Уровень заряда должен быть в диапазоне 0-100%")

        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def make_call(self, phone_number: str) -> bool:
        """
        Совершить звонок на указанный номер.

        :param phone_number: Номер телефона для звонка
        :return: True если звонок успешен, False если нет

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 50)
        >>> phone.make_call("+79991234567")
        True
        """
        # Здесь должна быть логика совершения звонка
        return bool(phone_number)

    def charge(self, percent: int) -> None:
        """
        Зарядить смартфон на указанный процент.

        :param percent: Процент заряда для добавления
        :raises ValueError: Если процент отрицательный или слишком большой

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 20)
        >>> phone.charge(30)
        >>> phone.battery_level
        50
        """
        if percent < 0:
            raise ValueError("Процент заряда не может быть отрицательным")
        if self.battery_level + percent > 100:
            raise ValueError("Уровень заряда не может превышать 100%")

        self.battery_level += percent


class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0) -> None:
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param owner_name: Имя владельца счета
        :param balance: Начальный баланс счета
        :raises ValueError: Если баланс отрицательный

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов И.И.", 1000.0)
        >>> account.account_number
        '40817810099910004312'
        >>> account.owner_name
        'Иванов И.И.'
        >>> account.balance
        1000.0
        """
        if balance < 0:
            raise ValueError("Баланс счета не может быть отрицательным")

        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Внести деньги на счет.

        :param amount: Сумма для внесения
        :raises ValueError: Если сумма отрицательная или равна нулю

        Примеры:
        >>> account = BankAccount("1234567890", "Петров П.П.", 500.0)
        >>> account.deposit(200)
        >>> account.balance
        700.0
        """
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")

        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Снять деньги со счета.

        :param amount: Сумма для снятия
        :return: True если снятие успешно, False если недостаточно средств
        :raises ValueError: Если сумма отрицательная или равна нулю

        Примеры:
        >>> account = BankAccount("0987654321", "Сидоров С.С.", 1000.0)
        >>> account.withdraw(500)
        True
        >>> account.balance
        500.0
        """
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            return False

        self.balance -= amount
        return True


if __name__ == "__main__":
    doctest.testmod()