class City:#создание класса City
    def __init__(self, name, population, area, country):#инициализация полей
        self._name = name
        self._population = population
        self._area = area
        self._country = country
#описание полей с использованием property и изменение их значей, используя setter-ы
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, value):
        self._population = value
    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, value):
        self._area = value
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, value):
        self._country = value
#Создание объекта класса
city = City('Гродно', 358717, 2511.87, 'Беларусь')
#Изменение свойств объекта класса
city.name = 'Минск'
city.population = 1996553
city.area = 409.5
city.country = 'Беларусь'
#Вывод свойств объекта класса
print(f'Название города: {city.name}')
print(f'Население города: {city.population}')
print(f'Площадь города: {city.area} км²')
print(f'Страна: {city.country}')
