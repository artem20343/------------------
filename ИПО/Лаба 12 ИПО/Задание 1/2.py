# Определение класса Student (студент)
class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name  # Имя и фамилия студента
        self.group_number = group_number  # Номер группы
        self.grades = grades  # Оценки студента

    def has_failing_grade(self):
        return any(grade < 3 for grade in self.grades)

# Создание списка students (студентов)
students = []

# Ввод информации о студентах
for _ in range(10):
    full_name = input("Введите ФИО студента: ")
    group_number = input("Введите номер группы: ")

    grades = []
    # Ввод оценок и проверка на корректность
    for i in range(5):
        while True:
            try:
                grade = int(input(f"Введите оценку за предмет {i + 1}: "))
                if 2 <= grade <= 5:
                    grades.append(grade)
                    break
                else:
                    print("Оценка должна быть в диапазоне от 2 до 5.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

    students.append(Student(full_name, group_number, grades))

# Поиск и вывод студентов с неудовлетворительными оценками
found_students = False
for student in students:
    if student.has_failing_grade():
        print(f"Студент: {student.full_name}, Группа: {student.group_number}")
        found_students = True

if not found_students:
    print("Нет студентов с неудовлетворительными оценками.")
