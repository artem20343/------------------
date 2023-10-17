<<<<<<< HEAD
import random

class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
        name (str): Фамилия и имя студента.
        group_number (str): Номер группы студента.
        academic_perfomance (list): Список оценок студента (список из пяти элементов).
    """

    def __init__(self, name, group_number, academic_perfomance):
        """
        Инициализирует новый экземпляр класса Student.

        Аргументы:
            name (str): Фамилия и имя студента.
            group_number (str): Номер группы студента.
            academic_perfomance (list): Список оценок студента (список из пяти элементов).
        """
        self.name = name
        self.group_number = group_number
        self.academic_perfomance = academic_perfomance
        self.gpa_scores = sum(self.academic_perfomance) / 5

    def print_info(self):
        """
        Выводит информацию о студенте, включая ФИ, номер группы, успеваемость и средний балл.
        """
        print(f'ФИ: {self.name}\n'
              f'  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_perfomance}\n'
              f'  Средний балл: {self.gpa_scores}\n')

def byGPA_key(student):
    """
    Функция-ключ для сортировки списка студентов по среднему баллу.

    Аргументы:
        student (Student): Экземпляр класса Student.

    Returns:
        float: Средний балл студента.
    """
    return student.gpa_scores
=======
import random

class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
        name (str): Фамилия и имя студента.
        group_number (str): Номер группы студента.
        academic_perfomance (list): Список оценок студента (список из пяти элементов).
    """

    def __init__(self, name, group_number, academic_perfomance):
        """
        Инициализирует новый экземпляр класса Student.

        Аргументы:
            name (str): Фамилия и имя студента.
            group_number (str): Номер группы студента.
            academic_perfomance (list): Список оценок студента (список из пяти элементов).
        """
        self.name = name
        self.group_number = group_number
        self.academic_perfomance = academic_perfomance
        self.gpa_scores = sum(self.academic_perfomance) / 5

    def print_info(self):
        """
        Выводит информацию о студенте, включая ФИ, номер группы, успеваемость и средний балл.
        """
        print(f'ФИ: {self.name}\n'
              f'  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_perfomance}\n'
              f'  Средний балл: {self.gpa_scores}\n')

def byGPA_key(student):
    """
    Функция-ключ для сортировки списка студентов по среднему баллу.

    Аргументы:
        student (Student): Экземпляр класса Student.

    Returns:
        float: Средний балл студента.
    """
    return student.gpa_scores
>>>>>>> ed71ffae37781bd81cd840534a288057e66a6392
