import requests  # Импорт библиотеки requests для выполнения HTTP-запросов

link = "https://icanhazip.com"  # URL-ссылка на веб-сайт, который возвращает IP-адрес клиента

responce = requests.get(link)  # Выполнение GET-запроса к указанному URL. В ответе содержится IP-адрес клиента

print(responce.status_code)  # Вывод статуса ответа HTTP. Если статус равен 200, это означает, что запрос был успешным

print(responce.text)  # Вывод текста ответа, который содержит IP-адрес клиента
