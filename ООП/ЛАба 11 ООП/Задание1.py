# Определение базового класса "Person", представляющего человека
class Person:
    def __init__(self, name, age):
        # Инициализация атрибутов объекта: имя и возраст
        self.name = name
        self.age = age

    def __str__(self):
        # Форматированный вывод информации о человеке
        return f"Person: {self.name}, Age: {self.age}"

# Определение класса "Employee", наследующего от класса "Person" и представляющего сотрудника
class Employee(Person):
    def __init__(self, name, age, position, salary):
        # Вызов конструктора базового класса "Person" с использованием super()
        super().__init__(name, age)
        # Инициализация атрибутов объекта: должность и зарплата
        self.position = position
        self.salary = salary

    def __str__(self):
        # Форматированный вывод информации о сотруднике
        return f"Employee: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"

# Определение класса "Father", наследующего от класса "Person" и представляющего отца
class Father(Person):
    def __init__(self, name, age, children=None):
        # Вызов конструктора базового класса "Person" с использованием super()
        super().__init__(name, age)
        # Инициализация атрибута объекта: список детей
        self.children = ", ".join(children) if children else None

    def __str__(self):
        # Форматированный вывод информации о отце
        return f"Father: {self.name}, Age: {self.age}, Children: {self.children}"

# Определение класса "WorkingFather", наследующего одновременно от "Employee" и "Father"
class WorkingFather(Employee, Father):
    def __init__(self, name, age, position, salary, children=None):
        # Явный вызов конструкторов базовых классов с использованием super()
        Employee.__init__(self, name, age, position, salary)
        Father.__init__(self, name, age, children)

    def __str__(self):
        # Форматированный вывод информации о работающем отце
        return f"Working Father: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Children: {self.children}"

# Пример использования
person = Person("John", 30)
print(person)

employee = Employee("Alice", 25, "Manager", 50000)
print(employee)

father = Father("Bob", 40, ["Tom", "Emma"])
print(father)

working_father = WorkingFather("David", 35, "Engineer", 60000, ["Sophia", "Liam"])
print(working_father)
