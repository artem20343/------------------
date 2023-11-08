# Определение базового класса Transport
class Transport:
    # Базовый класс, представляющий транспорт
    
    # Конструктор класса
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    # Метод для преобразования объекта в строку
    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"

# Определение класса Car, унаследованного от класса Transport
class Car(Transport):
    # Класс, представляющий автомобиль, унаследованный от класса Transport
    
    # Конструктор класса
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self._gasoline_residue = gasoline_residue
    
    # Геттер для свойства gasoline
    @property
    def gasoline(self):
        return f"Осталось бензина на {self._gasoline_residue} км"
    
    # Сеттер для свойства gasoline
    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self._gasoline_residue += value
            print(f"Объем топлива увеличен на {value} л и составляет {self._gasoline_residue} л")
        else:
            print("Ошибка заправки автомобиля")

# Определение класса Boat, унаследованного от класса Transport
class Boat(Transport):
    # Класс, представляющий лодку, унаследованный от класса Transport
    
    # Конструктор класса
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name
    
    # Метод для преобразования объекта в строку
    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"

# Определение класса Plane, унаследованного от класса Transport
class Plane(Transport):
    # Класс, представляющий самолет, унаследованный от класса Transport
    
    # Конструктор класса
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity
    
    # Метод для преобразования объекта в строку
    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"