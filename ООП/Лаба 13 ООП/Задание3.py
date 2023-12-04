# Импорт модулей tkinter и random
from tkinter import *
import random

# Определение функции throw_dice
def throw_dice():
    # Генерация случайного числа от 1 до 6
    dice_result = random.randint(1, 6)
    # Изменение текста метки на сгенерированное число
    lab.configure(text = str(dice_result))

# Создание графического окна
window = Tk()
# Установка заголовка окна
window.title("Брось кубик")
# Установка размеров окна
window.geometry('300x100')

# Создание метки с текстом "Брось кубик"
lab = Label(window, text="Брось кубик", fg='blue', font=('Arial', 17))
# Размещение метки в окне
lab.pack()

# Создание кнопки "Бросить кубик"
btn = Button(window, text='Бросить кубик', font=('Arial', 17), command=throw_dice)
# Размещение кнопки в окне
btn.pack()

# Запуск главного цикла обработки событий
window.mainloop()
