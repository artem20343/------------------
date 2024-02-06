import requests  # Импорт библиотеки requests для выполнения HTTP-запросов
import json  # Импорт библиотеки json для работы с JSON-данными

result = requests.get("https://swapi.dev/api/people/3/")  # Выполнение GET-запроса к API Star Wars для получения данных о персонаже с ID 3

if result.status_code == 200:  # Проверка статуса ответа HTTP. Если статус равен 200, это означает, что запрос был успешным
    json_dict = json.loads(result.text)  # Десериализация JSON-ответа в словарь Python

    json_dict['name'] = input("Введите имя: ")  # Запрос у пользователя ввести имя, которое затем добавляется в словарь

    with open("swap.json", "w") as file:  # Открытие файла "swap.json" для записи
        json_text = json.dump(json_dict, file, indent=4)  # Сериализация словаря Python обратно в JSON и запись в файл

    # Дополнительно:
    result_homeworld = requests.get(json_dict['homeworld'])  # Выполнение GET-запроса к URL 'homeworld' из исходного JSON-ответа
    print(result_homeworld.text)  # Вывод текста ответа на запрос 'homeworld'
