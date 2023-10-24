class Vector:
    def __init__(self, *args): 
        # Конструктор принимает переменное число аргументов
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)
        self.values.sort()
    
    def __str__(self):
        # Возвращает строковое представление вектора
        if len(self.values) == 0:
            return 'пустой вектор'
        return f'вектор{tuple(self.values)}'
    
    def add(self, other):
        # Складывает два вектора или вектор и скаляр
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('сложение векторов разной длины недопустимо.')            
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] + other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя сложить с {other}')
    
    def mul(self, other):
        # Умножает два вектора или вектор и скаляр
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('умножение векторов разной длины недопустимо.')            
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] * other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя умножить с {other}')

# Создаем объекты векторов и выполняем операции
v1 = Vector(1, 2, 3) # Создаем объект вектора v1
print(v1)
v2 = Vector(4, 7, 1, 12)
print(v2)    
v3 = Vector(7, 11, 3, 18)
print(v3)  
print(v2.add(v3)) # Складываем v2 и v3
print(v2.mul(v3)) # Умножаем v2 и v3