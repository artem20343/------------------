from tkinter import *

# Функция для закрытия окна
def close_window(): 
    window.destroy()

# Создание главного окна
window = Tk()

# Задание заголовка окна
window.title("Проект 1")

# Задание размеров окна
window.geometry('400x100')

# Создание метки
lab = Label(window, text="Моя первая программа", font=('Arial', 14))
lab.pack()

# Создание кнопки закрытия
btn = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)
btn.pack()

# Запуск цикла обработки событий
window.mainloop()