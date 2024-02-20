# Импортируем библиотеку numpy
import numpy as np

# Определение функции для вычисления определителя матрицы
def calculate_determinant(matrix):
    # Вычисляем и возвращаем определитель матрицы
    return np.linalg.det(matrix)

# Определение функции для решения системы уравнений
def solve_system(A, b):
    # Решаем систему уравнений и возвращаем результат
    return np.linalg.solve(A, b)

# Определение матрицы A
A = np.array([[3, 1], [1, 2]])

# Определение вектора b
b = np.array([9, 8])

# Выводим определитель матрицы A
print("Определитель матрицы A:", calculate_determinant(A))

# Выводим решение системы уравнений
print("Решение системы уравнений:", solve_system(A, b))
