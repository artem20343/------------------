# Создаем функцию-декоратор для проверки типа значения свойства
def validate_property_type(property_type):
    # Декоратор принимает функцию, для которой будет выполняться проверка
    def decorator(func):
        # Обертка вокруг функции для добавления проверки типа
        def wrapper(self, value):
            # Проверяем, соответствует ли значение указанному типу
            if not isinstance(value, property_type):
                # Если тип не соответствует, вызываем исключение
                raise ValueError(f"Invalid value for property {func.__name__}(). Expected {property_type}, got {type(value)}")
            # Если тип соответствует, вызываем оригинальную функцию
            return func(self, value)
        return wrapper
    return decorator

# Определяем класс City
class City:
    # Инициализируем свойства класса
    def __init__(self, name, population, country, famous_landmarks):
        self._name = name
        self._population = population
        self._country = country
        self._famous_landmarks = famous_landmarks
    
    # Определяем геттер и сеттер для свойства name
    @property
    def name(self):
        return self._name
    
    @name.setter
    # Применяем функцию-декоратор для проверки типа значения свойства
    @validate_property_type(str)
    def name(self, value):
        self._name = value
    
    # Определяем геттер и сеттер для свойства population
    @property
    def population(self):
        return self._population
    
    @population.setter
    # Применяем функцию-декоратор для проверки типа значения свойства
    @validate_property_type(int)
    def population(self, value):
        self._population = value
    
    # Определяем геттер и сеттер для свойства country
    @property
    def country(self):
        return self._country
    
    @country.setter
    # Применяем функцию-декоратор для проверки типа значения свойства
    @validate_property_type(str)
    def country(self, value):
        self._country = value
    
    # Определяем геттер и сеттер для свойства famous_landmarks
    @property
    def famous_landmarks(self):
        return self._famous_landmarks
    
    @famous_landmarks.setter
    # Применяем функцию-декоратор для проверки типа значения свойства
    @validate_property_type(list)
    def famous_landmarks(self, value):
        self._famous_landmarks = value

city = City("Москва", 12655050, "Россия", ["Красная площадь", "Московский Кремль"])
print(city.name)  # Выведет: Москва

city.name = "Санкт-Петербург"  # Задаем новое значение свойства name
print(city.name)  # Выведет: Санкт-Петербург

city.population = "неправильное значение" # Попытка задать неправильное значение
# Будет вызвано исключение ValueError с соответствующим сообщением об ошибке

city.famous_landmarks = "неправильное значение" # Попытка задать неправильное значение
# Будет вызвано исключение ValueError с соответствующим сообщением об ошибкой