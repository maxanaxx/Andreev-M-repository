import doctest
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Создание и подготовка к работе объекта "Книга"

        title: Название книги (не должно быть пустым)
        author: Автор книги (не должно быть пустым)
        pages: Количество страниц (должно быть положительным числом)

        Примеры:
        >>> book = Book("Война и мир", "Л.Н. Толстой", 1225)
        """
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
    def read_page(self, page_number: int) -> str:
        """
        Прочитать указанную страницу книги.
        page_number: Номер страницы для чтения

        Returns: Содержимое страницы (заглушка)

        Raises: Если номер страницы вне допустимого диапазона

        Примеры:
        >>> book = Book("Мастер и Маргарита", "М. Булгаков", 480)
        """
        if page_number < 1 or page_number > self.pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.pages}")
        return f"Содержимое страницы {page_number}"
        ...

    def get_book_info(self) -> dict:
        """
        Получить информацию о книге.

        Returns: Словарь с информацией о книге

        Примеры:
        >>> book = Book("Преступление и наказание", "Ф. Достоевский", 672)
        """
        ...

class Smartphone:
    def __init__(self, brand: str, model: str, battery_level: int = 100) -> None:
        """
        Создание и подготовка к работе объекта "Смартфон"

        brand: Бренд смартфона
        model: Модель смартфона
        battery_level: Уровень заряда батареи (0-100%)

        Raises: Если уровень заряда вне диапазона 0-100

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 80)
        """
        if not 0 <= battery_level <= 100:
            raise ValueError("Уровень заряда должен быть в диапазоне 0-100%")

        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def make_call(self, phone_number: str) -> bool:
        """
        Совершить звонок на указанный номер.
        phone_number: Номер телефона для звонка

        Returns: True если звонок успешен, False если нет

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 50)
        """
        ...

    def charge(self, percent: int) -> None:
        """
        Зарядить смартфон на указанный процент.
        percent: Процент заряда для добавления

        Raises: Если процент отрицательный или слишком большой

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 20)
        """
        if percent < 0:
            raise ValueError("Процент заряда не может быть отрицательным")
        if self.battery_level + percent > 100:
            raise ValueError("Уровень заряда не может превышать 100%")

        self.battery_level += percent
        ...


class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0) -> None:
        """
        Создание и подготовка к работе объекта "Банковский счет"
        account_number: Номер счета
        owner_name: Имя владельца счета
        balance: Начальный баланс счета

        Raises: сли баланс отрицательный

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов И.И.", 1000.0)
        """
        if balance < 0:
            raise ValueError("Баланс счета не может быть отрицательным")

        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Внести деньги на счет.
        amount: Сумма для внесения

        Raises: Если сумма отрицательная или равна нулю

        Примеры:
        >>> account = BankAccount("1234567890", "Петров П.П.", 500.0)
        """
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")

        self.balance += amount
        ...

    def withdraw(self, amount: float) -> bool:
        """
        Снять деньги со счета.
        amount: Сумма для снятия

        Returns: True если снятие успешно, False если недостаточно средств

        Примеры:
        >>> account = BankAccount("0987654321", "Сидоров С.С.", 1000.0)
        """
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            return False

        self.balance -= amount
        return True
        ...


if __name__ == "__main__":
    doctest.testmod()