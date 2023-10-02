import math

def calculate_circle_a(r):

    a = math.pi * r ** 2  # Формула для вычисления площади круга (pi * r^2)
    return a

# Запрос радиуса у пользователя
r = float(input("Введите радиус круга: "))

# Вычисление площади круга, вызывая функцию calculate_circle_a
a = calculate_circle_a(r)

# Вывод результата
print("Площадь круга: ", a)
