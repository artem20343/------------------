import requests  # Импорт библиотеки requests для выполнения HTTP-запросов

link = "https://browser-info.ru/"  # URL-ссылка на веб-сайт, который предоставляет информацию о браузере пользователя

responce = requests.get(link).text  # Выполнение GET-запроса к указанному URL и сохранение текста ответа

# Открытие файла "1.html" в указанной директории на запись с использованием кодировки UTF-8
with open("C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 22 ИПО\\1.html", "w", encoding="utf-8") as file:
    file.write(responce)  # Запись текста ответа в файл
