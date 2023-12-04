# Создание класса Интернет-магазин
class InternetShop:
    # Инициализация атрибутов
    def __init__(self, name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name):
        self.name = name
        self.product_name = product_name
        self.country = country
        self.payment_method = payment_method
        self.purchase_amount = purchase_amount
        self.sale_date = sale_date
        self.buyer_name = buyer_name

    # Метод для вывода информации о товаре
    def display_info(self):
        print("Название магазина:", self.name)
        print("Название продукта:", self.product_name)
        print("Город:", self.country)
        print("Способ оплаты:", self.payment_method)
        print("Сумма покупки:", self.purchase_amount)
        print("Дата продажи:", self.sale_date)
        print("Имя покупателя:", self.buyer_name)


# Создание дочернего класса Мебель для гостиной
class LivingRoomFurniture(InternetShop):
    # Инициализация дополнительных атрибутов для мебели гостиной
    def __init__(self, name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name, price, furniture_type, manufacturer):
        super().__init__(name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price
        self.furniture_type = furniture_type
        self.manufacturer = manufacturer


# Создание дочернего класса Кухонная мебель
class KitchenFurniture(InternetShop):
    # Инициализация дополнительных атрибутов для кухонной мебели
    def __init__(self, name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name, price, length, height, width, material):
        super().__init__(name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price
        self.length = length
        self.height = height
        self.width = width
        self.material = material


# Создание дочернего класса Ванная мебель
class BathroomFurniture(InternetShop):
    # Инициализация дополнительных атрибутов для ванной мебели
    def __init__(self, name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name, price):
        super().__init__(name, product_name, country, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price


# Создание экземпляров каждого класса и вывод информации о них
living_room_furniture1 = LivingRoomFurniture("Магазин мебели ABC", "Комплект диванов", "США", "Кредитная карта", 1500, "2022-01-15", "Джон Доу", 1200, "Диван", "Компания ABC мебели")
kitchen_furniture1 = KitchenFurniture("Магазин мебели XYZ", "Кухонный стол", "Германия", "PayPal", 800, "2022-01-20", "Джейн Смит", 500, 150, 75, 90, "Дерево")
bathroom_furniture1 = BathroomFurniture("123 Ванные комнаты", "Туалетный шкаф", "Китай", "Банковский перевод", 300, "2022-01-25", "Майкл Джонсон", 250)

living_room_furniture1.display_info()
kitchen_furniture1.display_info()
bathroom_furniture1.display_info()