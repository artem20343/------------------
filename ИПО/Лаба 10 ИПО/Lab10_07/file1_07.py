3# Ввод N и запись введенных чисел в file1_07.txt
N = int(input("Введите количество чисел (N): "))

with open("file1_07.txt", "w") as file1:
    for i in range(N):
        number = int(input(f"Введите число {i + 1}: "))
        file1.write(str(number) + "\n")

# Чтение чисел из file1_07.txt и вычисление среднего арифметического четных чисел
even_sum = 0  # Сумма четных чисел
even_count = 0  # Количество четных чисел

with open("file1_07.txt", "r") as file1:
    for line in file1:
        number = int(line.strip())
        if number % 2 == 0:
            even_sum += number
            even_count += 1

if even_count > 0:
    even_average = even_sum / even_count
else:
    even_average = 0

# Запись среднего арифметического четных чисел в file2_07.txt
with open("file2_07.txt", "w") as file2:
    file2.write(f"Среднее арифметическое четных чисел: {even_average}")

print(f"Среднее арифметическое четных чисел: {even_average} записано в file2_07.txt.")
