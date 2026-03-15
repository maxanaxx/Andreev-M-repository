class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        _brand (str): Марка транспортного средства (непубличный).
        _model (str): Модель транспортного средства (непубличный).
        _year (int): Год выпуска.
    """

    def __init__(self, brand, model, year):
        """
        Инициализация транспортного средства.

        Аргументы:
            brand: Марка.
            model: Модель.
            year: Год выпуска.
        """
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self):
        """Возвращает удобочитаемое строковое представление."""
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self):
        """Возвращает формальное строковое представление для разработчиков."""
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self._year})"

    def start_engine(self):
        """
        Запускает двигатель.

        Возвращает:
            str: Сообщение о запуске двигателя.
        """
        return f"Двигатель {self._brand} {self._model} запущен."

    def info(self):
        """
        Возвращает общую информацию о транспортном средстве.

        Возвращает:
            str: Описание ТС.
        """
        return f"Это транспортное средство: {self}"


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    Дополнительные атрибуты:
        _doors (int): Количество дверей (непубличный).
    """

    def __init__(self, brand, model, year, doors):
        """
        Расширение конструктора базового класса.

        Аргументы:
            brand: Марка.
            model: Модель.
            year: Год выпуска.
            doors: Количество дверей.
        """
        super().__init__(brand, model, year)
        self._doors = doors

    def __str__(self):
        """Перегружает __str__ для добавления информации о количестве дверей."""
        return f"{super().__str__()} с {self._doors} дверьми"

    def __repr__(self):
        """Перегружает __repr__ для учёта дочерних атрибутов."""
        return f"Car(brand='{self._brand}', model='{self._model}', year={self._year}, doors={self._doors})"

    def start_engine(self):
        """
        Перегрузка метода start_engine.

        Причина перегрузки:
            Для легкового автомобиля можно добавить дополнительное действие
            (например, проверка дверей перед запуском).
        """
        return f"Легковой автомобиль {self._brand} {self._model}: проверка дверей выполнена. Двигатель запущен."

    def info(self):
        """
        Наследует метод info без изменений (демонстрация наследования метода).
        """
        return super().info()


class Truck(Vehicle):
    """
    Дочерний класс для грузовых автомобилей.

    Дополнительные атрибуты:
        _capacity (float): Грузоподъёмность в тоннах (непубличный).
    """

    def __init__(self, brand, model, year, capacity):
        """
        Расширение конструктора базового класса.

        Аргументы:
            brand: Марка.
            model: Модель.
            year: Год выпуска.
            capacity: Грузоподъёмность (тонны).
        """
        super().__init__(brand, model, year)
        self._capacity = capacity

    def __str__(self):
        """Перегружает __str__ для отображения грузоподъёмности."""
        return f"{super().__str__()} грузоподъёмностью {self._capacity} т"

    def __repr__(self):
        """Перегружает __repr__ для учёта дочерних атрибутов."""
        return f"Truck(brand='{self._brand}', model='{self._model}', year={self._year}, capacity={self._capacity})"

    def start_engine(self):
        """
        Перегрузка метода start_engine.

        Причина перегрузки:
            Для грузового автомобиля требуется предварительная проверка тормозной системы.
        """
        return f"Грузовик {self._brand} {self._model}: проверка тормозной системы выполнена. Двигатель запущен."

    def info(self):
        """
        Наследует метод info без изменений (демонстрация наследования метода).
        """
        return super().info()


if __name__ == "__main__":
    # Примеры использования (только для демонстрации, реализация необязательна)
    car = Car("Toyota", "Corolla", 2020, 4)
    truck = Truck("Volvo", "FH", 2019, 20.5)

    print(car)
    print(repr(car))
    print(car.start_engine())
    print(truck)
    print(repr(truck))
    print(truck.start_engine())
    print(car.info())