def sm(arr):
    mi = arr.index(min(arr))
    ma = arr.index(max(arr))
    arr[mi], arr[ma] = arr[ma], arr[mi]
    return arr

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sm(array)
print("Массив после перестановки минимального и максимального элементов:", result)