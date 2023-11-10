class Rub(object):
    #Класс для работы с рублями и копейками.

    def __init__(self, rub=0, kop=0):
        #Инициализация объекта с указанием рублей и копеек.
        self.rub = rub
        self.kop = kop
        self.normalize()

    def normalize(self):
        #Приведение рублей и копеек к нормальному виду (копейки < 100).
        self.rub += self.kop // 100
        self.kop %= 100

    def __str__(self):
        #Преобразование объекта в строку для вывода.
        return f'{self.rub:03d}.{self.kop:02d} rub'

    def __lt__(self, other):
        #Сравнение двух объектов по стоимости.
        if self.rub == other.rub:
            return self.kop < other.kop
        return self.rub < other.rub

    def __add__(self, other):
        #Сложение двух объектов.
        res = Rub(self.rub + other.rub, self.kop + other.kop)
        res.normalize()
        return res


class Goods(object):
    #Класс описания товара: название и цена.

    def __init__(self, name='', rub=0, kop=0):
        #Инициализация объекта товара с указанием названия, рублей и копеек.
        self.name = name
        self.price = Rub(rub, kop)


# Считываем данные и создаем список товаров
goods_list = []
total_price = Rub()

while True:
    try:
        input_line = input()
        if not input_line:
            break
        name, price_str, _ = input_line.split()
        rub, kop = map(int, price_str.split('.'))
        goods_list.append(Goods(name, rub, kop))
        total_price += Rub(rub, kop)
    except ValueError:
        print("Некорректный формат ввода.")

# Сортируем список товаров по цене
goods_list.sort(key=lambda goods: goods.price, reverse=True)

# Выводим отсортированный список товаров и их стоимость
for goods in goods_list:
    print(f'{goods.name} {goods.price}')

# Выводим общую стоимость обеда
print(f'Total: {total_price}')