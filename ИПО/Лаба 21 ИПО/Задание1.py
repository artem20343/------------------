# Импорт необходимых библиотек
import requests
from bs4 import BeautifulSoup
import csv

# URL-адрес веб-страницы, с которой будут извлекаться данные
url = "https://www.belinvestbank.by/exchange-rates/courses-tab-group1?town=Минск&type=atm&latitude=54.4231189&longitude=25.9366916&showList=map&display=office"

# Заголовки запроса
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'}

# Отправка GET-запроса к веб-странице
r = requests.get(url, headers = user_agent)

# Парсинг HTML-кода веб-страницы
soup = BeautifulSoup(r.text, "html.parser")

# Поиск всех строк таблицы на веб-странице
items = soup.find_all("tr")

# Удаление первой строки таблицы (заголовка)
if items:
    items.pop(0)

# Создание словаря для хранения информации о валютах
curr = {}

# Обход каждой строки таблицы
for item in items:
    # Извлечение ячеек из строки
    _item = item.find_all("td")
    if _item:
        # Извлечение и обработка данных из ячеек
        curs = _item[2].get_text(strip=True).replace('.',',') if len(_item) > 2 else ""
        buy = _item[4].get_text(strip=True).replace('.',',') if len(_item) > 4 else ""
        sell = _item[5].get_text(strip=True).replace('.',',') if len(_item) > 5 else ""
        # Добавление информации о валюте в словарь
        curr[curs] = {
            'Покупка': buy,
            'Продажа': sell
        }

# Открытие файла для записи данных
with open('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 21 ИПО\\currs.csv', 'w', newline='') as file:
    # Создание объекта writer для записи данных в файл
    writer = csv.DictWriter(
        file,
        fieldnames=['Валюта', 'Продажа', 'Покупка'],
        delimiter=';',
        quoting=csv.QUOTE_MINIMAL
    )
    # Запись заголовка таблицы
    writer.writeheader()
    # Обход каждой валюты в словаре
    for curs, info in curr.items():
        # Запись информации о валюте в файл
        writer.writerow({'Валюта': curs, **info})
