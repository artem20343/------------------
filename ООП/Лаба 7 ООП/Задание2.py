# Создаем класс A
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def c(self):
        return 3 * (self.a ** 3) + self.b

# Пример использования класса
objA = A(2, 4)
print(objA.c)  # Вывод значения свойства c, вычисленного на основе a и b
