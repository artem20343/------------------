def cd(arr):
    se = 0
    p = 1

    for i, num in enumerate(arr):
        if i % 2 == 0:
            se += num
        else:
            p *= num

    return se, p

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
se, p = cd(array)
print("Сумма элементов с четными номерами:", se)
print("Произведение элементов с нечетными номерами:", p)