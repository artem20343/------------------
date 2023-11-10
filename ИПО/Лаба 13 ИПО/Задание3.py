# Считываем данные и создаем список товаров
goods_list = []
total_price = Rub()

while True:
    try:
        input_line = input()
        if not input_line:
            break
        name, price_str = input_line.split()
        rub, kop = map(int, price_str.split('.'))
        goods_list.append(Goods(name, rub, kop))
        total_price += Rub(rub, kop)
    except ValueError:
        print("Некорректный формат ввода.")

# Сортируем список товаров по цене
goods_list.sort(key=lambda goods: goods.price, reverse=True)

# Выводим отсортированный список товаров
for goods in goods_list:
    print(f'{goods.name} {goods.price}')

# Выводим общую стоимость
print(f'total {total_price}')

# Спрашиваем у пользователя, сколько денег он дал
t = input('tender: ')
tender_rub, tender_kop = map(int, t.split('.'))

# Создаем объект для предоставленной суммы
tender_amount = Rub(tender_rub, tender_kop)
print(f'tender {tender_amount}')

# Вычисляем и выводим сдачу
change = tender_amount - total_price
print(f'change {change}')