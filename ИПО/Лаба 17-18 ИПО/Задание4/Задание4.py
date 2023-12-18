from PIL import Image, ImageFilter

# Открываем изображение
img = Image.open('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание4\\image3_22.jpg')

# Применяем фильтр к изображению
img_filtered = img.filter(ImageFilter.FIND_EDGES)

# Сохраняем отфильтрованное изображение под новым именем
img_filtered.save('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание4\\image4_22.jpg')

# Применяем несколько фильтров к изображению
img_multi_filtered = img.filter(ImageFilter.FIND_EDGES)
img_multi_filtered = img_multi_filtered.filter(ImageFilter.SMOOTH_MORE)

# Сохраняем отфильтрованное изображение под новым именем
img_multi_filtered.save('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание4\\image44_22.jpg')