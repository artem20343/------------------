from tkinter import *  # Импортирует все классы и функции из модуля tkinter
from tkinter import ttk  # Импортирует модуль ttk, который содержит некоторые дополнительные виджеты

window = Tk()  # Создает новое окно
window.geometry("300x80")  # Устанавливает размер окна 300x80

value_var = IntVar()  # Создает переменную целого типа для отслеживания прогресса

# Создает горизонтальный прогресс-бар с длиной 280 и привязанной переменной value_var
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate')  
pb.pack()  # Размещает прогресс-бар в окне

def start(): pb.start(100)  # Функция для запуска прогресс-бара
def stop(): pb.stop()  # Функция для остановки прогресс-бара

# Создает кнопку "Start", которая вызывает функцию start при нажатии
start_btn = ttk.Button(text="Start", command=start)  
start_btn.pack()  # Размещает кнопку "Start" в окне

# Создает кнопку "Stop", которая вызывает функцию stop при нажатии
stop_btn = ttk.Button(text="Stop", command=stop)  
stop_btn.pack()  # Размещает кнопку "Stop" в окне

window.mainloop()  # Запускает основной цикл обработки событий
