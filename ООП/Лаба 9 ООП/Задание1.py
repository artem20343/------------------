# Определение класса Rectangle
class Rectangle:
    def __init__(self, a, b):
        self.a = a  # Задаем длину стороны a
        self.b = b  # Задаем длину стороны b

    def get_area(self):
        return self.a * self.b  # Вычисляем площадь прямоугольника

# Определение класса Square
class Square:
    def __init__(self, a):
        self.a = a  # Задаем длину стороны a

    def get_area(self):
        return self.a ** 2  # Вычисляем площадь квадрата

# Определение класса Circle
class Circle:
    def __init__(self, r):
        self.r = r  # Задаем радиус r

    def get_area(self):
        return 3.14 * self.r ** 2  # Вычисляем площадь круга

# Создаем экземпляры классов
rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 3)
sql = Square(2)
cirl = Circle(3)

# Собираем все фигуры в список
figures = [rect1, rect2, sql, cirl]

# Выводим площади всех фигур
for figure in figures:
    print(figure.get_area())
