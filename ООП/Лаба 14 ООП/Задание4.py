import tkinter as tk  # Импортирует модуль tkinter для создания графического интерфейса
from tkinter import ttk  # Импортирует модуль ttk для использования тем оформления tkinter
import numpy as np  # Импортирует модуль numpy для работы с числовыми данными
import math  # Импортирует модуль math для выполнения математических операций

# Определяет функцию для табулирования и обновления прогресса
def tabulate_and_update():  
    x_values = np.arange(0.01, 0.9, 0.01)  # Создает массив значений x от 0.01 до 0.9 с шагом 0.01
    listbox.delete(0, tk.END)  # Очищает listbox перед началом табулирования
    progress['value'] = 0  # Сбрасывает прогресс до 0
    
    # Для каждого значения x в массиве x_values
    for x in x_values:  
        y = math.sin(2*x + 1)  # Вычисляет значение y, используя функцию sin
        listbox.insert(tk.END, f"x: {x:.2f}, y: {y:.2f}")  # Добавляет пару (x, y) в listbox
        progress['value'] += (1/len(x_values))*100  # Обновляет прогресс
        root.update_idletasks()  # Обновляет интерфейс

root = tk.Tk()  # Создает новое окно
root.title("Расчет функции")  # Устанавливает заголовок окна

frame_input = ttk.Frame(root)  # Создает новый фрейм в окне
frame_input.grid(column=0, row=0)  # Размещает фрейм в окне

label_function = ttk.Label(frame_input, text="y=sin(2*x+1)")  # Создает метку с текстом функции
label_function.grid(column=0, row=0)  # Размещает метку в фрейме

# Создает кнопку "Расчет", которая вызывает функцию tabulate_and_update при нажатии
button_calculate = ttk.Button(frame_input, text="Расчет", command=tabulate_and_update)  
button_calculate.grid(column=1,row=1)  # Размещает кнопку в фрейме

listbox = tk.Listbox(root)  # Создает новый listbox в окне
listbox.grid(column=0,row=2)  # Размещает listbox в окне

# Создает новый прогресс-бар в окне
progress = ttk.Progressbar(root,length=200,value=20,maximum=100)  
progress.grid(columnspan=root.grid_size()[0],row=root.grid_size()[1])  # Размещает прогресс-бар в окне

root.mainloop()  # Запускает основной цикл обработки событий
