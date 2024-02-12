# Определение функции balance_array, которая принимает одномерный массив в качестве аргумента
def balance_array(arr):
    # Подсчет количества положительных элементов в массиве
    pos_count = sum(1 for num in arr if num > 0)
    # Подсчет количества отрицательных элементов в массиве
    neg_count = sum(1 for num in arr if num < 0)

    # Если положительных элементов больше, добавляем отрицательные элементы
    if pos_count > neg_count:
        arr.extend([-1] * (pos_count - neg_count))
    # Если отрицательных элементов больше, добавляем положительные элементы
    elif neg_count > pos_count:
        arr.extend([1] * (neg_count - pos_count))

    # Возвращаем измененный массив
    return arr

# Создание исходного массива для демонстрации работы функции
arr = [1, -2, 3, -4, 5]
# Вызов функции balance_array и сохранение результата в переменной balanced_arr
balanced_arr = balance_array(arr)
# Вывод результата на экран
print(balanced_arr)
