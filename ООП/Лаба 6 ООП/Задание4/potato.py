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
        stages = ["Росток", "Зелёная", "Зрелая"]
        return stages[self.stage]

    def grow(self):
        """
        Увеличивает стадию зрелости картошки на одну.
        """
        if self.stage < 2:
            self.stage += 1