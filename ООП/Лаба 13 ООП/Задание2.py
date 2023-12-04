# Импорт всего из модуля tkinter
from tkinter import *

# Определение функции clicked
def clicked():
    # Изменение текста метки
    lab.configure(text = 'Первые успехи')

# Определение функции close_window
def close_window():
    # Закрытие окна
    window.destroy()

# Создание графического окна
window = Tk()
# Установка заголовка окна
window.title("Проект 2")
# Установка размеров окна
window.geometry('400x100')

# Создание метки
lab = Label(window, text="", font=('Arial', 14))
# Размещение метки в окне
lab.grid(column=1, row=0)

# Создание кнопки Приветствие
btn = Button(window, text='Приветствие', font=('Arial', 14), command=clicked)
# Размещение кнопки Приветствие в окне
btn.grid(column=0, row=1)

# Создание кнопки Закрыть
btn1 = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)
# Размещение кнопки Закрыть в окне
btn1.grid(column=2, row=1)

# Запуск главного цикла обработки событий
window.mainloop()
