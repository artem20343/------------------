# Импортируем необходимые функции из модуля urllib.parse
from urllib.parse import urlparse, urlunparse

# Задаем URL-адрес, который нужно разобрать и затем собрать обратно
url = 'https://informburo.kz:443/interview/cto-takoe-passivnaya-svetskost-i-pocemu-ona-vazna-dlya-kazaxstana'

# Разбираем URL-адрес на составляющие
result = urlparse(url)

# Собираем URL-адрес обратно из элементов кортежа
reconstructed_url = urlunparse(result)

# Выводим полученный URL-адрес на печать
print(reconstructed_url)
