import math

def calculate_rectangle_area(length, width):
    """Вычисляет площадь прямоугольника."""
    return length * width

def calculate_right_triangle_area(base, height):
    """Вычисляет площадь прямоугольного треугольника."""
    return 0.5 * base * height

def calculate_quadrilateral_area(X, Y, Z, T):
    """Вычисляет площадь четырехугольника."""
    # Площадь прямоугольного треугольника (X, Y, гипотенуза)
    triangle_area = calculate_right_triangle_area(X, Y)

    # Площадь прямоугольника (ширина Z, высота T)
    rectangle_area = calculate_rectangle_area(Z, T)

    # Общая площадь четырехугольника
    quadrilateral_area = triangle_area + rectangle_area
    return quadrilateral_area

# Входные данные: длины сторон четырехугольника
X = float(input("Введите длину стороны X: "))
Y = float(input("Введите длину стороны Y: "))
Z = float(input("Введите длину стороны Z: "))
T = float(input("Введите длину стороны T: "))

# Вычисление площади четырехугольника
area = calculate_quadrilateral_area(X, Y, Z, T)

print("Площадь четырехугольника: {:.2f}".format(area))