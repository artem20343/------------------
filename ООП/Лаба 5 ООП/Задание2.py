# Создание класса Vector
class Vector:
    # Конструктор класса, принимает два аргумента x и y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод для вычисления модуля вектора
    def calculate_module(self):
        module = (self.x ** 2 + self.y ** 2) ** 0.5
        return module

    # Метод для умножения вектора на константу k
    def multiply_by_constant(self, k):
        new_x = k * self.x
        new_y = k * self.y
        return Vector(new_x, new_y)

# Создание объекта класса Vector с координатами (3, 4)
vector = Vector(3, 4)

# Вычисление модуля вектора
module = vector.calculate_module()

# Умножение вектора на константу 2
multiplied_vector = vector.multiply_by_constant(2)

# Вывод результата
print("|вектор| =", module)
print("k*|вектор| =", multiplied_vector.x, multiplied_vector.y)