from student import Student, byGPA_key
import random
 
def main():
    # Создаем список студентов
    students = [
        Student(
            input('Введите фамилию и имя студента: '),
            input('Введите номер группы: '),
            [random.randint(1, 10) for i_grade in range(5)]
        )
        for i_student in range(10)
    ]
    # Сортируем студентов по среднему баллу
    students_sort = sorted(students, key=byGPA_key)
    for student in students_sort: # Выводим информацию о каждом студенте
        student.print_info()

if __name__ == "__main__":
=======
from student import Student, byGPA_key
import random
 
def main():
    # Создаем список студентов
    students = [
        Student(
            input('Введите фамилию и имя студента: '),
            input('Введите номер группы: '),
            [random.randint(1, 10) for i_grade in range(5)]
        )
        for i_student in range(10)
    ]
    # Сортируем студентов по среднему баллу
    students_sort = sorted(students, key=byGPA_key)
    for student in students_sort: # Выводим информацию о каждом студенте
        student.print_info()

if __name__ == "__main__":
>>>>>>> ed71ffae37781bd81cd840534a288057e66a6392
    main()