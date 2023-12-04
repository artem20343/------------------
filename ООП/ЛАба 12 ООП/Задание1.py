class Collection:#создание класса коллекция
    def __init__(self, name, owner):#инициализация полей
        self.name = name
        self.owner = owner
class MusicAlbum:#создание класса музыкальный альбом
    def __init__(self, author, genre, year, duration):#инициализация полей
        self.author = author
        self.genre = genre
        self.year = year
        self.duration = duration
class MusicPiece:#создание класса музыкальное произведение
    def __init__(self, name, duration):#инициализация полей
        self.name = name
        self.duration = duration
    def info(self):#метод по выводу информации
        try:
            if self.duration <= 0:#оповещает об ошибке если продолжительность <0 то выдаёт ошибку значения
                raise ValueError('длительность не может быть меньше либо равна 0')
            else:#в ином случае вывод
                print(f'Название: {self.name}\n'
                      f'Продолжительность: {self.duration} минут')
        except ValueError as e:
            print('Error:', str(e))
class Song(MusicPiece):#создание дочернего класса песня
    def __init__(self, name, duration, lyrics, lyricist):#инициализация полей
        super().__init__(name, duration)#наследование класса музыкальное произведение
        self.lyrics = lyrics
        self.lyricist = lyricist
    def info(self):#метод по выводу информации
        try:
            if self.duration <= 0:#оповещение об ошибке, если длительность <0, ошибка значения
                raise ValueError('длительность не может быть меньше либо равна 0')
            else:#в ином случае вывод
                print(f'Название: {self.name}\n'
                      f'Длительность: {self.duration} минут\n'
                      f'Текст: {self.lyrics}\n'
                      f'Автор текста: {self.lyricist}')
        except ValueError as e:
            print('Error:', str(e))
class InstrumentalPiece(MusicPiece):#создание дочернего класса инструментальное произведение
    def __init__(self, name, duration, instruments):#инициализация полей
        super().__init__(name, duration)#наследование класса музыкальное произведение
        self.instruments = instruments
    def info(self):#метод по выводу информации
        try:
            if self.duration <= 0:#оповещение об ошибке, если длительность <0, ошибка значения
                raise ValueError('длительность не может быть меньше либо равна 0')
            else:#в ином случае вывод
                print(f'Название: {self.name}\n'
                      f'Продолжительность: {self.duration} минут\n'
                      f'Инструменты: {self.instruments}')
        except ValueError as e:
            print('Error:', str(e))

# Создание коллекции
collection = Collection('Любимое', 'Роял Джордж')
# Создание альбома
album = MusicAlbum('Oberstleutnant', 'Rock', 1985, 60)
# Создание песни и проверка на наличие ошибки
song = Song('Gofrshtard', -3.14, 'Клирик', 'Отто Брэйт')
# Создание инструментального произведения
instrumental = InstrumentalPiece('Гальвара', 4.17, 'Полный оркестр')
# Генерация описания песни и инструментального произведения
song.info()
instrumental.info()
