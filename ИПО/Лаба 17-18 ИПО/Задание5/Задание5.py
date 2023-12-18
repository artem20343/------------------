from PIL import Image, ImageDraw, ImageFont

# Открываем изображение
img = Image.open('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание5\\image1_22.jpg')

# Создаем объект для рисования
draw = ImageDraw.Draw(img)

# Задаем шрифт и размер (вам может потребоваться указать путь к файлу шрифта на вашем компьютере)
font = ImageFont.truetype("arial.ttf", 15)

# Задаем текст и позицию
text = "Савич"
textwidth, textheight = draw.textsize(text, font)
position = (img.width - textwidth, 0)

# Рисуем текст и прямоугольник вокруг него
draw.text(position, text, font=font, fill="black")
draw.rectangle([position, (img.width, textheight)], outline="black")

# Сохраняем изображение под новым именем
img.save('C:\\Users\\Professional\\Desktop\\Пары\\Лабораторные работы\\GitHub\\ИПО\\Лаба 17-18 ИПО\\Задание5\\image5_22.jpg')
