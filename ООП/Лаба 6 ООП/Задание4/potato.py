<<<<<<< HEAD
class Potato:
    """
    Класс, представляющий картошку.
    """

    def __init__(self, number):
        """
        Инициализация объекта класса Potato.

        :param number: Номер картошки в грядке.
        """
        self.number = number
        self.stage = 0

    def get_stage(self):
        """
        Возвращает текущую стадию зрелости картошки.

        :return: Стадия зрелости.
        """
        stages = ["Росток","Росток", "Зелёная", "Зрелая"]
        return stages[self.stage]

    def grow(self):
        """
        Увеличивает стадию зрелости картошки на одну.
        """
        if self.stage < 3:
=======
class Potato:
    """
    Класс, представляющий картошку.
    """

    def __init__(self, number):
        """
        Инициализация объекта класса Potato.

        :param number: Номер картошки в грядке.
        """
        self.number = number
        self.stage = 0

    def get_stage(self):
        """
        Возвращает текущую стадию зрелости картошки.

        :return: Стадия зрелости.
        """
        stages = ["Росток","Росток", "Зелёная", "Зрелая"]
        return stages[self.stage]

    def grow(self):
        """
        Увеличивает стадию зрелости картошки на одну.
        """
        if self.stage < 3:
>>>>>>> ed71ffae37781bd81cd840534a288057e66a6392
            self.stage += 1