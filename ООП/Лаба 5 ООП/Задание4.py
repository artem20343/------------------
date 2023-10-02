# Создание класса Counter

class Counter:
    # Конструктор класса
    def __init__(self):
        self.value = 0

    # Метод для установки начального значения счетчика
    def start_from(self, value=0):
        self.value = value

    # Метод для увеличения значения счетчика на 1
    def increment(self):
        self.value += 1

    # Метод для вывода текущего значения счетчика
    def display(self):
        print(f'Текущее значение счетчика = {self.value}')

    # Метод для сброса значения счетчика в 0
    def reset(self):
        self.value = 0

# Создание экземпляра класса Counter
counter = Counter()

# Установка начального значения счетчика
counter.start_from(5)
counter.display()  # Вывод: Текущее значение счетчика = 5

# Увеличение значения счетчика на 1
counter.increment()
counter.display()  # Вывод: Текущее значение счетчика = 6

# Сброс значения счетчика в 0
counter.reset()
counter.display()  # Вывод: Текущее значение счетчика = 0