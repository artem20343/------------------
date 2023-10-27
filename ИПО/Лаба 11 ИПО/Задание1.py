# Определение класса MilitaryAircraft
class MilitaryAircraft:
    """
    Класс, описывающий военные воздушные суда.

    Атрибуты:
    - name (str): Название воздушного судна.
    - aircraft_type (str): Тип воздушного судна (истребитель, бомбардировщик, транспортник и т.д.).
    - max_speed (int): Максимальная скорость воздушного судна в км/ч.
    - range (int): Дальность полета воздушного судна в км.
    - weaponry (list): Список вооружения, установленного на воздушном судне.
    - crew (int): Количество членов экипажа.

    Методы:
    - display_info(): Выводит информацию о воздушном судне, включая название, тип, максимальную скорость и дальность полета.
    - add_weapon(weapon): Добавляет вооружение к списку weaponry.
    - remove_weapon(weapon): Удаляет указанное вооружение из списка weaponry.
    - change_crew_size(new_crew_size): Изменяет количество членов экипажа.
    """

    def __init__(self, name, aircraft_type, max_speed, aircraft_range, weaponry, crew):
        # Инициализация атрибутов класса
        self.name = name
        self.aircraft_type = aircraft_type
        self.max_speed = max_speed
        self.range = aircraft_range
        self.weaponry = weaponry
        self.crew = crew

    def display_info(self):
        # Метод для вывода информации о воздушном судне
        print(f"Воздушное судно: {self.name}")
        print(f"Тип: {self.aircraft_type}")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Дальность полета: {self.range} км")
        print(f"Вооружение: {', '.join(self.weaponry)}")
        print(f"Экипаж: {self.crew} человек\n")

    def add_weapon(self, weapon):
        # Метод для добавления вооружения к списку weaponry
        self.weaponry.append(weapon)

    def remove_weapon(self, weapon):
        # Метод для удаления указанного вооружения из списка weaponry
        if weapon in self.weaponry:
            self.weaponry.remove(weapon)

    def change_crew_size(self, new_crew_size):
        # Метод для изменения количества членов экипажа
        self.crew = new_crew_size

# Создание экземпляров класса
aircraft1 = MilitaryAircraft("Su-27", "Истребитель", 2450, 3300, ["Ракеты", "Пушки"], 1)
aircraft2 = MilitaryAircraft("Tu-160", "Бомбардировщик", 2200, 12000, ["Ядерные бомбы", "Крылатые ракеты"], 5)
aircraft3 = MilitaryAircraft("C-130", "Транспортник", 671, 3335, ["Парашютисты", "Груз"], 3)
aircraft4 = MilitaryAircraft("F-35", "Истребитель", 1930, 2222, ["Ракеты", "Бортовой пушки"], 1)
aircraft5 = MilitaryAircraft("A-10", "Штурмовик", 706, 3900, ["Авиабомбы", "Пушки", "Ракеты"], 1)

# Вывод документации класса
print(MilitaryAircraft.__doc__)

# Вывод информации о каждом созданном экземпляре
aircraft1.display_info()
aircraft2.display_info()
aircraft3.display_info()
aircraft4.display_info()
aircraft5.display_info()

# Пример использования методов
aircraft1.add_weapon("Лазеры")
aircraft1.display_info()

aircraft3.remove_weapon("Парашютисты")
aircraft3.change_crew_size(5)
aircraft3.display_info()
