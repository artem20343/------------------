<<<<<<< HEAD
from product import Product

# Создаем массив объектов класса Product
products = [
    Product("Молоко", "Домик в деревне", 50.0, 7, 10),
    Product("Хлеб", "Хлебный двор", 30.0, 5, 20),
    Product("Яблоки", "Сады Придонья", 80.0, 14, 15)
]

# Выводим список товаров, срок хранения которых больше заданного
shelf_life_limit = 10

print(f"Товары со сроком хранения больше {shelf_life_limit} дней:")
for product in products:
    if product.shelf_life > shelf_life_limit:
        product.print_info()
=======
from product import Product

# Создаем массив объектов класса Product
products = [
    Product("Молоко", "Домик в деревне", 50.0, 7, 10),
    Product("Хлеб", "Хлебный двор", 30.0, 5, 20),
    Product("Яблоки", "Сады Придонья", 80.0, 14, 15)
]

# Выводим список товаров, срок хранения которых больше заданного
shelf_life_limit = 10

print(f"Товары со сроком хранения больше {shelf_life_limit} дней:")
for product in products:
    if product.shelf_life > shelf_life_limit:
        product.print_info()
>>>>>>> ed71ffae37781bd81cd840534a288057e66a6392
        print()