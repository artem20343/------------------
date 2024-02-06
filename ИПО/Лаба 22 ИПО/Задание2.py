import requests  # Импорт библиотеки requests для выполнения HTTP-запросов
import json  # Импорт библиотеки json для работы с JSON-данными

result = requests.get("https://swapi.dev/api/films/1/")  # Выполнение GET-запроса к API Star Wars для получения данных о фильме с ID 1

json_dict = json.loads(result.text)  # Десериализация JSON-ответа в словарь Python

print(json_dict["opening_crawl"])  # Вывод текста открывающегося текста из полученного словаря
