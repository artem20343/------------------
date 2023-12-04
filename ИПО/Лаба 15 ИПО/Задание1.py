# Импортируем необходимые модули
import random  # Модуль для генерации случайных чисел
import timeit  # Модуль для измерения времени выполнения
from prettytable import PrettyTable  # Модуль для создания красивых таблиц

def slow_func(arr):
    """
    Функция slow_func выполняет сортировку списка методом обмена по убыванию.
    :param arr: Список, который требуется отсортировать.
    :return: Отсортированный список.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_test(sort_func, num_elements):
    """
    Функция sort_test выполняет сортировку списка указанным способом и возвращает время выполнения.
    :param sort_func: Функция сортировки, которую необходимо протестировать.
    :param num_elements: Количество элементов в списке.
    :return: Отсортированный список и время выполнения в секундах.
    """
    # Генерируем список случайных чисел
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    
    # Измеряем время выполнения сортировки
    start_time = timeit.default_timer()
    sorted_arr = sort_func(arr)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    
    return sorted_arr, execution_time

# Размеры списков, для которых будем проверять время сортировки
num_elements_arr = [10, 100, 1000, 10000, 100000]

# Создаем таблицу и задаем заголовки столбцов
table = PrettyTable(["Размер списка", "Время выполнения (сек)"])

# Проходимся по каждому размеру списка и тестируем сортировку
for num_elements in num_elements_arr:
    sorted_arr, execution_time = sort_test(slow_func, num_elements)
    table.add_row([num_elements, execution_time])

# Выводим таблицу
print(table)