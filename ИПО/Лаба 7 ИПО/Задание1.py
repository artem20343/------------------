streets = ["ул. Красная", "ул. Ленина", "ул. Победы", "ул. Гагарина", "ул. Притыцкого", "ул. Независимости", "ул. Железнодорожная"]
# Создаем список streets, содержащий названия улиц.

tu = tuple(streets)
# Преобразуем список streets в кортеж tu.

new_tu = tu[:3]
# Создаем новый кортеж new_tu, содержащий первые три элемента из кортежа tu.

new_tu2 = tu[3:]
# Создаем новый кортеж new_tu2, содержащий оставшиеся элементы из кортежа tu, начиная с четвертого элемента.

all_tu = (tu, new_tu, new_tu2)
# Создаем новый кортеж all_tu, содержащий исходный кортеж tu, а также новые кортежи new_tu и new_tu2.

print(new_tu)
# Выводим на экран содержимое кортежа new_tu.

print(new_tu2)
# Выводим на экран содержимое кортежа new_tu2.

print(all_tu)
# Выводим на экран содержимое кортежа all_tu.