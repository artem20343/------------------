from rectangle import calculate_rectangle_area
from triangle import calculate_right_triangle_area

def calculate_quadrilateral_area(X, Y, Z, T):
    """Вычисляет площадь четырехугольника."""
    # Площадь прямоугольного треугольника (X, Y, гипотенуза)
    triangle_area = calculate_right_triangle_area(X, Y)

    # Площадь прямоугольника (ширина Z, высота T)
    rectangle_area = calculate_rectangle_area(Z, T)

    # Общая площадь четырехугольника
    quadrilateral_area = triangle_area + rectangle_area
    return quadrilateral_area