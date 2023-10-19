class City:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

class Country:
    def __init__(self, cities):
        self.cities = cities

    def sort_cities_by_population(self):
        self.cities.sort(key=lambda city: city.population)

    def find_cities_by_area(self, min_area, max_area):
        return [city for city in self.cities if min_area <= city.area <= max_area]

# Создаем несколько объектов-городов
city1 = City("Минск", 1975326, 348.8)
city2 = City("Брест", 343985, 146.1)
city3 = City("Гродно", 368710, 142.1)
city4 = City("Гомель", 508839, 139.8) 
city5 = City("Витебск", 362466, 124.5)

# Создаем объект класса Country и помещаем в него города
country = Country([city1, city2, city3, city4, city5])

# Сортируем города по населению
country.sort_cities_by_population()

# Выводим информацию о городах после сортировки
print("\nГорода после сортировки по населению:")
for city in country.cities:
    print(f"{city.name}: Население - {city.population}, Площадь - {city.area} км²")

# Задаем диапазон площади для поиска городов
min_area = 140  # Минимальная площадь
max_area = 350  # Максимальная площадь

# Находим города, соответствующие заданному диапазону площади
cities_in_range = country.find_cities_by_area(min_area, max_area)

# Выводим города в заданном диапазоне площади
print(f"\nГорода со площадью от {min_area} км² до {max_area} км²:")
for city in cities_in_range:
    print(f"{city.name}: Площадь - {city.area} км²")
