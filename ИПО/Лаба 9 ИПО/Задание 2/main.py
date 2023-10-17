from geometry import calculate_quadrilateral_area

# Входные данные: длины сторон четырехугольника
X = float(input("Введите длину стороны X: "))
Y = float(input("Введите длину стороны Y: "))
Z = float(input("Введите длину стороны Z: "))
T = float(input("Введите длину стороны T: "))

# Вычисление площади четырехугольника
area = calculate_quadrilateral_area(X, Y, Z, T)

print("Площадь четырехугольника: {:.2f}".format(area))