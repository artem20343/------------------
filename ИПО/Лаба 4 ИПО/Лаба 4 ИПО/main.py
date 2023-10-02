s = input("Введите строку:\n")
string = ''
flag = 1

for i in range(len(s)):
    if s[i] != ' ':
        string += s[i]

print("Обработанная строка:", string)

# Находим длину половины строки
half_length = len(string) // 2

# Заменяем буквы 'п' на звездочки в первой половине строки
string = string[:half_length].replace('п', '*') + string[half_length:]

print("Строка с замененными 'п' на звездочки в первой половине:", string)

# Проверка на палиндром
for i in range(half_length):
    if string[i] != string[-i - 1]:
        flag = 0
        break

if flag:
    print("Это палиндром.")
else:
    print("Это не палиндром.")
