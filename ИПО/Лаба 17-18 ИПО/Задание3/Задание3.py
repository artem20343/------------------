from PIL import Image

# Открываем изображение
img = Image.open('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание3\\image2_22.jpg')

# Задаем координаты для обрезки (левый верхний угол, правый нижний угол)
# В этом примере мы обрезаем изображение, оставляя центральную часть
width, height = img.size
left = width/4
top = height/4
right = 3 * width/4
bottom = 3 * height/4

# Обрезаем изображение
img_cropped = img.crop((left, top, right, bottom))

# Отображаем обрезанное изображение
img_cropped.show()

# Сохраняем обрезанное изображение под новым именем
img_cropped.save('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание3\\image3_22.jpg')
