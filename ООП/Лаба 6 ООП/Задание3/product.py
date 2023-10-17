<<<<<<< HEAD
class Product:
    """
    Класс, описывающий товар.

    Атрибуты:
    - name (str): наименование товара
    - manufacturer (str): производитель товара
    - price (float): цена товара
    - shelf_life (int): срок хранения товара в днях
    - quantity (int): количество товара

    Методы:
    - print_info(): выводит информацию о товаре
    """

    def __init__(self, name, manufacturer, price, shelf_life, quantity):
        """
        Конструктор класса.

        Аргументы:
        - name (str): наименование товара
        - manufacturer (str): производитель товара
        - price (float): цена товара
        - shelf_life (int): срок хранения товара в днях
        - quantity (int): количество товара
        """
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.shelf_life = shelf_life
        self.quantity = quantity

    def print_info(self):
        """
        Выводит информацию о товаре.
        """
        print(f"Название: {self.name}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Цена: {self.price} руб.")
        print(f"Срок хранения: {self.shelf_life} дней")
=======
class Product:
    """
    Класс, описывающий товар.

    Атрибуты:
    - name (str): наименование товара
    - manufacturer (str): производитель товара
    - price (float): цена товара
    - shelf_life (int): срок хранения товара в днях
    - quantity (int): количество товара

    Методы:
    - print_info(): выводит информацию о товаре
    """

    def __init__(self, name, manufacturer, price, shelf_life, quantity):
        """
        Конструктор класса.

        Аргументы:
        - name (str): наименование товара
        - manufacturer (str): производитель товара
        - price (float): цена товара
        - shelf_life (int): срок хранения товара в днях
        - quantity (int): количество товара
        """
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.shelf_life = shelf_life
        self.quantity = quantity

    def print_info(self):
        """
        Выводит информацию о товаре.
        """
        print(f"Название: {self.name}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Цена: {self.price} руб.")
        print(f"Срок хранения: {self.shelf_life} дней")
>>>>>>> ed71ffae37781bd81cd840534a288057e66a6392
        print(f"Количество: {self.quantity}")