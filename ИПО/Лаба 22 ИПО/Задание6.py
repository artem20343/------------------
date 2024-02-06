# Импортируем необходимые библиотеки
import requests
import fake_useragent
from bs4 import BeautifulSoup

# Создаем случайный user-agent с помощью библиотеки fake_useragent
user = fake_useragent.UserAgent().random
# Создаем заголовки для запроса, включая user-agent
header = {'user-agent': user}

# Ссылка на сайт, с которого мы хотим получить информацию
link = "https://browser-info.info.ru"
# Делаем GET-запрос к сайту и получаем текст ответа
response = requests.get(link, headers=header).text
# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response, 'xml')
# Находим блок с нужной информацией на странице
block = soup.find('div', id ="tool_padding")

# Проверяем, включен ли JavaScript
check_js = block.find('div', id ='javascript_check')
# Получаем статус JavaScript
status_js = check_js.find_all('span')[1].text
# Формируем строку с результатом
result_js = f'javascript: {status_js}'

# Проверяем версию Flash
check_flash = block.find('div', id ="flash version")
# Получаем статус Flash
status_flash = check_flash.find_all('span')[1].text
# Формируем строку с результатом
result_flash=f'flash: {status_flash}'

# Проверяем user-agent
check_user= block.find('div', id ="user_agent").text

# Выводим результаты
print(result_js)
print(result_flash)
print(check_user)

# Находим ссылку в блоке
link = block.find('a').get('href')
# Выводим ссылку
print(link)
