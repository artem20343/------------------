def print_numbers_in_string(input_string):
    """
    Функция, которая находит и выводит числа из строки, каждое число на новой строке.
    """
    current_number = ''  # Инициализация пустой строки для текущего числа

    # Проходим по каждому символу во входной строке
    for char in input_string:
        # Проверяем, является ли символ цифрой, точкой или знаком минуса (для отрицательных чисел)
        if char.isdigit() or char == '.' or (current_number and char == '-'):
            current_number += char  # Добавляем символ к текущему числу
        elif current_number:
            # Если текущее число не пустое, выводим его
            print(current_number)
            current_number = ''  # Сбрасываем текущее число

    # Выводим последнее число, если оно есть
    if current_number:
        print(current_number)

input_str = input('Введите строку: ')  # Получаем строку от пользователя
print('Числа в строке:')
print_numbers_in_string(input_str)  # Вызываем функцию для поиска и вывода чисел в строке

