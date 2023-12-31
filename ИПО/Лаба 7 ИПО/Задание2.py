# Создаем словарь "a" с ключами в виде дат и значениями в виде лабораторных работ.
a = {
    "01.01.2023": "Лабораторная работа 1",
    "02.01.2023": "Лабораторная работа 2",
    "03.01.2023": "Лабораторная работа 3",
    "04.01.2023": "Лабораторная работа 4",
    "05.01.2023": "Лабораторная работа 5",
    "06.01.2023": "Лабораторная работа 6",
    "07.01.2023": "Лабораторная работа 7"
}

# Выводим все элементы словаря a в формате "ключ - значение".
for key, value in a.items():
    print(key, "-", value)

# Просим пользователя ввести ключ для поиска значения.
search_key = input("Введите ключ для поиска значения: ")

# Проверяем, есть ли введенный ключ в словаре a.
if search_key in a:
    print("Значение по ключу", search_key, ":", a[search_key])
else:
    print("Ключ", search_key, "не найден")