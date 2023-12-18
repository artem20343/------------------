from PIL import Image

# Открываем изображение
img = Image.open('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание2\\image1_22.jpg')

# Поворачиваем изображение на 30 градусов по часовой стрелке
img_rotated = img.rotate(-30)

# Отображаем повернутое изображение
img_rotated.show()

# Сохраняем повернутое изображение под новым именем
img_rotated.save('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание2\\image2_22.jpg')
