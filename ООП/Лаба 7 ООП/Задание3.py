import random

class Flower:
    def __init__(self, stem_length, freshness):
        self.stem_length = stem_length
        self.freshness = freshness

    @property
    def stem_length(self):
        return self._stem_length

    @stem_length.setter
    def stem_length(self, value):
        if not isinstance(value, int):
            print('Длина стебля должна быть числом')
        elif value < 5:
            print('Длина стебля должна быть минимум 5')
        elif value > 20:
            print('Длина стебля должна быть максимум 20')
        else:
            self._stem_length = value

    @property
    def freshness(self):
        return self._freshness

    @freshness.setter
    def freshness(self, value):
        if not isinstance(value, int):
            print('Уровень свежести должен быть числом')
        elif value < 1:
            print('Уровень свежести должен быть минимум 1')
        elif value > 10:
            print('Уровень свежести должен быть максимум 10')
        else:
            self._freshness = value

# Создание списка объектов класса Flower с случайными значениями атрибутов
flowers = []
for _ in range(5):
    stem_length = random.randint(5, 20)
    freshness = random.randint(1, 10)
    flowers.append(Flower(stem_length, freshness))

print('Цветки (длина стебля, уровень свежести):')
for i, flower in enumerate(flowers, start=1):
    print(f'Цветок {i}: {flower.stem_length}, {flower.freshness}')

# Сортировка цветков по уровню свежести
sorted_flowers = sorted(flowers, key=lambda x: x.freshness)

# Вывод элементов отсортированного списка
print('\nОтсортированный букет:')
for i, flower in enumerate(sorted_flowers, start=1):
    print(f'Цветок {i} - уровень свежести: {flower.freshness}')

# Задание диапазона длин стеблей
start_length = int(input('Введите начальное значение диапазона: '))
end_length = int(input('Введите конечное значение диапазона: '))

# Вывод элементов списка в заданном диапазоне
print(f'\nЦветки с длиной стебля от {start_length} до {end_length}:')
filtered_flowers = [flower for flower in flowers if start_length <= flower.stem_length <= end_length]
for i, flower in enumerate(filtered_flowers, start=1):
    print(f'Цветок {i} - длина стебля: {flower.stem_length}')
