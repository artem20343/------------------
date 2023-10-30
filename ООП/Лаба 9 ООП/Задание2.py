# Определение класса Трапеция
class Trapezoid:
    # Конструктор класса Трапеция, инициализирует стороны трапеции и её высоту
    def __init__(self, side1, side2, side3, side4, height):
        self.side1 = side1  # Боковая сторона 1
        self.side2 = side2  # Боковая сторона 2
        self.side3 = side3  # Основание 1
        self.side4 = side4  # Основание 2
        self.height = height  # Высота трапеции

    # Метод для вычисления периметра трапеции
    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4


# Определение класса Ромб
class Rhombus:
    # Конструктор класса Ромб, инициализирует сторону ромба
    def __init__(self, side):
        self.side = side  # Сторона ромба

    # Метод для вычисления периметра ромба
    def perimeter(self):
        return 4 * self.side


# Определение класса Прямоугольник
class Rectangle:
    # Конструктор класса Прямоугольник, инициализирует длину и ширину
    def __init__(self, length, width):
        self.length = length  # Длина прямоугольника
        self.width = width    # Ширина прямоугольника

    # Метод для вычисления периметра прямоугольника
    def perimeter(self):
        return 2 * (self.length + self.width)


# Пример использования полиморфных методов для нахождения периметра разных фигур
trapezoid = Trapezoid(5, 7, 6, 8, 4)
rhombus = Rhombus(6)
rectangle = Rectangle(10, 5)

figures = [trapezoid, rhombus, rectangle]

for figure in figures:
    if isinstance(figure, Trapezoid):
        print(f'Периметр Трапеции: {figure.perimeter()}')
    elif isinstance(figure, Rhombus):
        print(f'Периметр Ромба: {figure.perimeter()}')
    elif isinstance(figure, Rectangle):
        print(f'Периметр Прямоугольника: {figure.perimeter()}')
