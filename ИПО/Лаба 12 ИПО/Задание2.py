class MilitaryAircraft:
    def __init__(self, aircraft_type, max_speed, max_range):
        self.__aircraft_type = aircraft_type
        self.__max_speed = max_speed
        self.__max_range = max_range

    def set_aircraft_type(self, aircraft_type):
        self.__aircraft_type = aircraft_type

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def set_max_range(self, max_range):
        self.__max_range = max_range

    def get_aircraft_type(self):
        return self.__aircraft_type

    def get_max_speed(self):
        return self.__max_speed

    def get_max_range(self):
        return self.__max_range

    def display_info(self):
        print("Тип воздушного судна:", self.get_aircraft_type())
        print("Максимальная скорость:", self.get_max_speed(), "км/ч")
        print("Максимальная дальность полета:", self.get_max_range(), "км")

    def __del__(self):
        print("Деструктор выполнился для военного воздушного судна.")

# Создание списка из 10 объектов MilitaryAircraft с использованием конструктора
aircraft_list = []
for i in range(10):
    aircraft_type = input("Введите тип военного воздушного судна: ")
    max_speed = float(input("Введите максимальную скорость (км/ч): "))
    max_range = float(input("Введите максимальную дальность полета (км): "))
    aircraft = MilitaryAircraft(aircraft_type, max_speed, max_range)
    aircraft_list.append(aircraft)

# Вывод информации о военных воздушных судах
for aircraft in aircraft_list:
    aircraft.display_info()

# Завершение программы, деструктор будет вызван для каждого объекта
