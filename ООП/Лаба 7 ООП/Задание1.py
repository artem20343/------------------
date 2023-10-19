# Создаем класс Train
class Train:
    def __init__(self, destination, train_number, departure_time, common_seats, compartments, reserved_seats):
        self._destination = destination
        self._train_number = train_number
        self._departure_time = departure_time
        self._common_seats = common_seats
        self._compartments = compartments
        self._reserved_seats = reserved_seats

    @property
    def destination(self):
        return self._destination

    @property
    def train_number(self):
        return self._train_number

    @train_number.setter
    def train_number(self, value):
        if isinstance(value, str):
            self._train_number = value
        else:
            raise ValueError("Номер поезда должен быть строкой")

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        if isinstance(value, str):
            self._departure_time = value
        else:
            raise ValueError("Время отправления должно быть строкой")

# Пример использования класса
train1 = Train("Минск", "12345", "08:00", 200, 50, 100)
print(train1.destination)  # Вывод пункта назначения (не инкапсулированное поле)
print(train1.train_number)  # Вывод номера поезда с использованием свойства
print(train1.departure_time)  # Вывод времени отправления с использованием свойства

# Изменение номера поезда через свойство
train1.train_number = "54321"
print(train1.train_number)  # Вывод обновленного номера поезда
