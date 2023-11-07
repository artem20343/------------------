class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name  # Фамилия и инициалы
        self.group_number = group_number  # Номер группы
        self.grades = grades  # Успеваемость (массив из пяти элементов)

    def get_average_grade(self):
        # Метод для вычисления средней оценки
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def display_info(self):
        # Метод для отображения информации о студенте
        print("ФИО:", self.full_name)
        print("Номер группы:", self.group_number)
        print("Успеваемость:", self.grades)
        print("Средний балл:", self.get_average_grade())

# Пример использования класса:
student1 = Student("Иванов И.И.", "Группа 101", [4, 5, 3, 4, 5])
student2 = Student("Петров П.П.", "Группа 102", [5, 4, 4, 3, 5])

student1.display_info()
student2.display_info()
