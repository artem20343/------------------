import numpy as np

# Генерируем случайное количество строк и столбцов от 15 до 100
rows = np.random.randint(15, 101)
cols = np.random.randint(15, 101)

# Создаем массив с указанным количеством строк и столбцов,
# заполняем его случайными целыми числами от 1 до 1000
array = np.random.randint(1, 1001, size=(rows, cols))

# Выводим массив на экран
np.set_printoptions(threshold=np.inf)
print("Массив:")
print(array)

# Находим максимальный элемент в каждом столбце
max_elements = np.max(array, axis=0)

# Выводим максимальные элементы на экран
print("Максимальные элементы в каждом столбце:")
print(max_elements)

# Вычисляем сумму всех элементов массива
sum_array = np.sum(array)

# Вычисляем сумму всех максимальных элементов
sum_max_elements = np.sum(max_elements)

# Вычисляем общую сумму
total_sum = sum_array + sum_max_elements

print("Сумма всех элементов массива и найденных максимальных элементов:", total_sum)
