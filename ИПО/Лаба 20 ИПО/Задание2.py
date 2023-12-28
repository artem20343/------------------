# Импортируем функцию urlparse из модуля urllib.parse
from urllib.parse import urlparse

# Задаем URL-адрес, который нужно разобрать
url = 'https://informburo.kz:443/interview/cto-takoe-passivnaya-svetskost-i-pocemu-ona-vazna-dlya-kazaxstana'

# Разбираем URL-адрес на составляющие
result = urlparse(url)

# Извлекаем протокол из разобранного URL-адреса
protocol = result.scheme

# Выводим протокол на печать
print(f"Протокол: {protocol}")
