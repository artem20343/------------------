from PIL import Image

# Открываем изображение
img = Image.open('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание1\\12.jpg')

# Отображаем изображение
img.show()

# Сохраняем изображение в том же формате под новым именем
img.save('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание1\\image1_22.jpg')

# Выводим характеристики изображения
print(f'Формат: {img.format}')
print(f'Размер: {img.size}')
print(f'Цветовой режим: {img.mode}')
