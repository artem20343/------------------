import requests  # Импорт библиотеки requests для выполнения HTTP-запросов
import json  # Импорт библиотеки json для работы с JSON-данными

# URL для получения информации о песчаном гусеничном велосипеде
url = "https://swapi.dev/api/vehicles/4/"  # URL API Star Wars для получения данных о транспортном средстве с ID 4

# Отправляем запрос на сервер
result = requests.get(url)  # Выполнение GET-запроса к указанному URL

# Проверяем успешность запроса
if result.status_code == 200:  # Проверка статуса ответа HTTP. Если статус равен 200, это означает, что запрос был успешным

    # Преобразуем полученные данные в JSON формат
    json_dict = json.loads(result.text)  # Десериализация JSON-ответа в словарь Python

    # Выводим информацию о стоимости песчаного гусеничного велосипеда
    print(f"Информация о песчаном гусеничном велосипеде:\n"
          f"Имя: {json_dict.get('name', 'Неизвестно')}\n"
          f"Стоимость: {json_dict.get('cost_in_credits', 'Неизвестно')} галактических кредитов")  # Вывод информации о транспортном средстве, включая его имя и стоимость в галактических кредитах
