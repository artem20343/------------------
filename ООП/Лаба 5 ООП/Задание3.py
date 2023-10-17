# Создание класса Student

class Student:
    # Конструктор класса
    def __init__(self, full_name, g_number, grades):
        self.full_name = full_name
        self.g_number = g_number
        self.grades = grades

    # Метод для вывода информации о студенте
    def print_info(self):
        print(f'ФИО: {self.full_name}\nНомер группы: {self.g_number}\nУспеваемость: {self.grades}')

# Создание списка студентов
students = [
    Student('Мишинков Иван Иванович', 'Группа 1', [4, 5, 3, 4, 5]),
    Student('Иванов Валерий Петрович', 'Группа 2', [3, 4, 5, 4, 3]),
    Student('Сидоров Павел Дмитриевич', 'Группа 1', [5, 5, 5, 5, 5]),
    Student('Морозов Егор Григорьевич', 'Группа 2', [2, 3, 4, 3, 2]),
    Student('Берета Николай Генадьевич', 'Группа 1', [4, 4, 4, 4, 4]),
    Student('Дмитриев Василий Игнатьевич', 'Группа 2', [5, 5, 5, 5, 5]),
    Student('Коваленко Никита Иванович', 'Группа 1', [3, 3, 3, 3, 3]),
    Student('Шабов Артем Александрович', 'Группа 2', [4, 4, 4, 4, 4]),
    Student('Антоненко Дмитрий Ильич', 'Группа 1', [2, 2, 2, 2, 2]),
    Student('Сергеев Максим Игоревич', 'Группа 2', [5, 5, 5, 5, 5])
]

# Вывод информации о студентах
for student in students:
    student.print_info()

# Сортировка списка студентов по возрастанию среднего балла
students.sort(key=lambda student: sum(student.grades) / len(student.grades))