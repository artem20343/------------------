class Rub(object):
     #Класс для работы с рублями и копейками.
    def __init__(self, rub=0, kop=0):
        self.rub = rub
        self.kop = kop
        self.normalize()

    def normalize(self):
        #Метод для нормализации значений копеек и рублей.
        self.rub += self.kop // 100
        self.kop %= 100

    def __str__(self):
        #Метод для форматированного вывода.
        return f"{self.rub:02d}.{self.kop:02d} rub"

    def __lt__(self, other):
        #Метод для сравнения объектов.
        if self.rub == other.rub:
            return self.kop < other.kop
        return self.rub < other.rub

    def __add__(self, other):
       # Метод для сложения объектов.
        res = Rub(self.rub + other.rub, self.kop + other.kop)
        res.normalize()
        return res

class Goods(object):
     #Класс описания товара: название и цена
    def __init__(self, name='', rub=0, kop=0):
        self.name = name
        self.price = Rub(rub, kop)

def process_goods_list(goods_list):
    #Функция для обработки списка товаров.
    # Сортировка товаров по цене от дорогих к дешевым
    sorted_goods = sorted(goods_list, key=lambda x: x.price, reverse=True)

    # Вывод товаров
    for good in sorted_goods:
        print(f"{good.name} {good.price}")

    # Вычисление общей стоимости
    total_price = Rub()
    for good in goods_list:
        total_price += good.price

    print(f"\n-----\ntotal {total_price}")

    # Запрос о сдаче
    tender = float(input("tender: "))
    tender_rub = int(tender)
    tender_kop = int((tender - tender_rub) * 100)
    tender_amount = Rub(tender_rub, tender_kop)

    # Вычисление и вывод сдачи
    change = tender_amount - total_price
    print(f"tender {tender_amount}")
    print(f"change {change}")

# Пример использования
goods_list = [
    Goods("rice", 10, 50),
    Goods("tea", 6, 30),
    Goods("cake", 10, 12),
    Goods("salad", 20, 0)
]

process_goods_list(goods_list)
