array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mp = float('-inf')

for row in array:
    for element in row:
        if element > 0 and element > mp:
            mp = element

if mp != float('-inf'):
    mp /= 2

print("Максимальный положительный элемент, деленный на 2:", mp)