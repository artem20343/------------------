class Drob(object):
    #Класс для представления дробей в виде целых числителя и знаменателя

    def __init__(self, a=0, b=1):
        #Инициализация объекта дроби с числителем a и знаменателем b
        self.a = a
        self.b = b
        self.normalize()

    def normalize(self):
       #Приведение дроби к каноническому виду
        gcd = self.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def gcd(self, x, y):
        #Нахождение наибольшего общего делителя
        while y != 0:
            x, y = y, x % y
        return x

    def __str__(self):
        #Преобразование объекта дроби в строку для вывода
        return '{}/{}'.format(self.a, self.b)

    def __eq__(self, other):
        #Проверка на равенство двух дробей
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        #Проверка, является ли одна дробь меньшей другой
        return self.a * other.b < self.b * other.a

    def __add__(self, other):
        #Сложение двух дробей
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __sub__(self, other):
        #Вычитание одной дроби из другой
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __mul__(self, other):
        #Умножение двух дробей
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __truediv__(self, other):
        #Деление одной дроби на другую
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Drob(new_a, new_b)


# Проверка функций
drob1 = Drob(1, 2)
drob2 = Drob(3, 4)

print(drob1 == drob2)   # False
print(drob1 < drob2)    # True
print(drob1 + drob2)    # 5/4
print(drob1 - drob2)    # -1/4
print(drob1 * drob2)    # 3/8
print(drob1 / drob2)    # 2/3