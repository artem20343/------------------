# Импорт модуля tkinter
from tkinter import *

# Функция для расчета дохода
def calculate_income():
    # Получение введенных пользователем данных
    initial_amount = float(initial_amount_entry.get())
    term_days = int(term_days_entry.get())
    interest_rate = float(interest_rate_entry.get())
    interest_type = interest_type_var.get()

    # Расчет дохода в зависимости от типа процентов
    if interest_type == 'Простые проценты':
        # Расчет простых процентов
        income = initial_amount + (initial_amount * interest_rate / 100) * term_days
    elif interest_type == 'Сложные проценты':
        # Расчет сложных процентов
        income = initial_amount * ((1 + interest_rate / 100) ** term_days)

    # Вывод расчетов
    income_label.configure(text = str(income))
    total_amount_label.configure(text = str(initial_amount + income))

# Создание окна
window = Tk()
window.title("Расчет дохода по вкладу")
window.geometry('300x400')

# Создание и размещение элементов интерфейса
initial_amount_label = Label(window, text="Сумма")
initial_amount_label.grid(column=0, row=1)
initial_amount_entry = Entry(window)
initial_amount_entry.grid(column=1, row=1)

term_days_label = Label(window, text="Срок(дней)")
term_days_label.grid(column=0, row=2)
term_days_entry = Entry(window)
term_days_entry.grid(column=1, row=2)

interest_rate_label = Label(window, text="Процентная ставка")
interest_rate_label.grid(column=0, row=3)
interest_rate_entry = Entry(window)
interest_rate_entry.grid(column=1, row=3)

# Создание переменной для хранения типа процентов
interest_type_var = StringVar()
interest_type_var.set('Простые проценты')

# Создание рамки для выбора типа процентов
interest_type_frame = LabelFrame(window, text="Схема начисления процентов", padx=50, pady=20)
interest_type_frame.grid(column=0, row=4, columnspan=2, padx=30, pady=30)

# Создание радиокнопок для выбора типа процентов
simple_interest_rb = Radiobutton(interest_type_frame, text='Простые проценты', variable=interest_type_var, value='Простые проценты')
simple_interest_rb.pack(anchor=W)

compound_interest_rb = Radiobutton(interest_type_frame, text='Сложные проценты', variable=interest_type_var, value='Сложные проценты')
compound_interest_rb.pack(anchor=W)

# Создание кнопки для запуска расчета
calculate_button = Button(window, text='Вычислить', font=('Arial', 14), width=9, padx=70, pady=1, command=calculate_income)
calculate_button.grid(column=0, row=5, columnspan=2)

# Создание меток для вывода результатов
income_word_label = Label(window, text="Доход:")
income_word_label.grid(column=0, row=6, columnspan=2)

income_label = Label(window, text="")
income_label.grid(column=0, row=7, columnspan=2)

total_amount_word_label = Label(window, text="Сумма в конце срока вклада:")
total_amount_word_label.grid(column=0, row=8, columnspan=2)

total_amount_label = Label(window, text="")
total_amount_label.grid(column=0, row=9, columnspan=2)

# Запуск главного цикла обработки событий
window.mainloop()
