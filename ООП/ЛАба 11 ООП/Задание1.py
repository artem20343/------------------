class Person:#создание класса человек
    def __init__(self, name, age):#инициализация полей класса человек
        self.name = name
        self.age = age
    def __str__(self):#возвращает имя и возраст
        return f'Name: {self.name}, Age: {self.age}'
class Worker(Person):#создание класса работник
    def __init__(self, name, age, profession):#инициализация полей класса работник
        super().__init__(name, age)#наследование полей класса человек
        self.profession = profession
    def __str__(self):#возвращает имя, возраст и профессию
        return f'Name: {self.name}, Age: {self.age}, Profession: {self.profession}'
class Father(Person):#создание класса отец
    def __init__(self, name, age, children=2):#инициализация полей класса отец
        super().__init__(name, age)#наследование полей класса человек
        self.children = children
    def __str__(self):#возвращет имя, возраст и количество детей
        return f'Name: {self.name}, Age: {self.age}, Children: {self.children}'
class WorkingFather(Worker, Father):#создание класса работник-отец
    def __init__(self, name, age, profession, children):#инициализация полей класса работник-отец
        Worker.__init__(self, name, age, profession)#наследование полей класса работник
        Father.__init__(self, name, age, children)#наследование полей класса отец
    def __str__(self):#возвращает имя, возраст, профессия и кол-во детей
        return f'Name: {self.name}, Age: {self.age}, Profession: {self.profession}, Children: {self.children}'
#создание объектов классов и проверка работоспособности
person = Person('John Smith', 30)
print(person)
worker = Worker('Peter Brown', 40, 'Engineer')
print(worker)
father = Father('Michael Johna', 46, 2)
print(father)
working_father = WorkingFather('Roberto de Davidos', 26, 'Teacher', 1)
print(working_father)
