# Импорт модулей tkinter и random
from tkinter import *
import random
import math

# Определение функции calculate
def calculate():
    # Получение значения X из текстового поля
    x = float(entry_x.get())
    # Вычисление выражения
    result = (math.sqrt(x) * math.sin(x**2/2) - 1.3) / (x**(1/5) + math.exp(3*x) + abs(math.cos(x)))
    # Вывод результата в метку
    label_result.configure(text = str(result))

# Создание графического окна
window = Tk()
# Установка заголовка окна
window.title("Формула")
# Установка размеров окна
window.geometry('300x200')

# Создание метки с текстом "Подсчет по формуле"
lab = Label(window, text="Подсчет по формуле", fg='blue', font=('Arial', 15))
# Размещение метки в окне
lab.pack()

# Создание метки "x ="
label_x = Label(window, text="x =", font=('Arial', 14))
# Размещение метки в окне
label_x.place(x=30, y=40)

# Создание текстового поля для ввода X
entry_x = Entry(window, font=('Arial', 14), width=10)
# Размещение текстового поля в окне
entry_x.place(x=90, y=40)

# Создание кнопки "Вычислить"
btn = Button(window, text='Вычислить', font=('Arial', 14), width=9, command=calculate)
# Размещение кнопки в окне
btn.place(x=92, y=70)

# Создание метки "Выражение ="
label_v = Label(window, text="Выражение =", font=('Arial', 14))
# Размещение метки в окне
label_v.place(x=30, y=110)

# Создание метки для вывода результата
label_result = Label(window, text="", font=('Arial', 14))
# Размещение метки в окне
label_result.place(x=150, y=110)

# Запуск главного цикла обработки событий
window.mainloop()