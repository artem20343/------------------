# Импорт всех функций из модуля tkinter
from tkinter import *
# Импорт модуля ttk из tkinter
from tkinter import ttk

# Определение функции getInfo
def getInfo():
    # Вывод имени
    print('Имя: ', nameT.get())
    # Вывод фамилии
    print('Фамилия: ', lastNameT.get())
    # Проверка и вывод пола
    if polvar.get() == 'm':
        print('Пол: мужской')
    elif polvar.get() == 'w':
        print('Пол: женский')
    else:
        print('Пол не указан')
    # Вывод любимых предметов
    print('Любимые предметы: ')
    if var1.get() == 1:
        print(' - математика')
    if var2.get() == 1:
        print(' - английский язык')
    if var3.get() == 1:
        print(' - информационные технологии')

# Создание окна
window = Tk()
# Установка заголовка окна
window.title('Регистрация')
# Создание и настройка метки имени
name = Label(window, text = 'Имя', width = 20, height = 1, fg = 'blue', font = 'arial 18')
# Создание и настройка метки фамилии
lastName = Label(window, text = 'Фамилия', width = 20, height = 1, fg = 'blue', font = 'arial 18')
# Создание и настройка метки пола
pol = Label(window, text = 'Пол', width = 20, height = 1, fg = 'blue', font = 'arial 18')
# Создание и настройка метки любимых предметов
likePr = Label(window, text = 'Любимые предметы', width = 20, height = 1, fg = 'blue', font = 'arial 18')

# Создание и настройка поля ввода имени
nameT = Entry(window, width = 30, font = 'arial 14')
# Создание и настройка поля ввода фамилии
lastNameT = Entry(window, width = 30, font = 'arial 14')
# Создание и настройка переменной для радиокнопок пола
polvar = StringVar()
polvar.set(' ')
# Создание и настройка радиокнопки мужского пола
radio1 = Radiobutton(window, text = 'мужской', variable = polvar, value = 'm')
# Создание и настройка радиокнопки женского пола
radio2 = Radiobutton(window, text = 'женский', variable = polvar, value = 'w')
# Создание и настройка переменных для флажков любимых предметов
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
# Создание и настройка флажка математики
check1 = Checkbutton(window, text = 'математика', variable = var1, onvalue = 1, offvalue = 0)
# Создание и настройка флажка английского языка
check2 = Checkbutton(window, text = 'английский язык', variable = var2, onvalue = 1, offvalue = 0)
# Создание и настройка флажка информационных технологий
check3 = Checkbutton(window, text = 'информационные технологии', variable = var3, onvalue = 1, offvalue = 0)
# Создание и настройка кнопки "Принять"
btn = Button(window, text = 'Принять', width = 25, height = 5, fg = 'blue', font = 'arial 14', command = getInfo)
# Размещение элементов в окне
name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()
# Запуск главного цикла обработки событий
window.mainloop()
