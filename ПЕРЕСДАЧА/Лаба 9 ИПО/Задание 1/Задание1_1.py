import math

# Функция для вычисления площади прямоугольного треугольника
def area_of_right_triangle(a, b):
    return 0.5 * a * b

# Функция для вычисления площади прямоугольника
def area_of_rectangle(a, b):
    return a * b

# Функция для вычисления площади квадрата
def area_of_square(a):
    return a * a

# Функция для вычисления площади четырехугольника
def area_of_quadrilateral(x, y, z, t):
    # Если все стороны равны, то это квадрат
    if x == y == z == t:
        quadrilateral_area = area_of_square(x)
    else:
        # Найдем площадь прямоугольного треугольника
        triangle_area = area_of_right_triangle(x, y)

        # Найдем площадь прямоугольника
        rectangle_area = area_of_rectangle(z, t)

        # Площадь четырехугольника равна сумме площадей треугольника и прямоугольника
        quadrilateral_area = triangle_area + rectangle_area

    return quadrilateral_area

# Ввод значений сторон четырехугольника
x = float(input("Введите значение стороны x: "))
y = float(input("Введите значение стороны y: "))
z = float(input("Введите значение стороны z: "))
t = float(input("Введите значение стороны t: "))

# Вычисление и вывод площади четырехугольника
result = area_of_quadrilateral(x, y, z, t)
print("Площадь четырехугольника:", result)
