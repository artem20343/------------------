# Импортируем функцию urlparse из модуля urllib.parse
from urllib.parse import urlparse

# Задаем URL-адрес
url = 'https://informburo.kz:443/interview/cto-takoe-passivnaya-svetskost-i-pocemu-ona-vazna-dlya-kazaxstana'

# Применяем функцию urlparse к URL-адресу
result = urlparse(url)

# Выводим результат
print(result)
