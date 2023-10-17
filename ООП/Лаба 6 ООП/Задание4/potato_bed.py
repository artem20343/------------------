from potato import Potato

class PotatoBed:
    """
    Класс, представляющий грядку картошки.
    """

    def __init__(self, num_potatoes):
        """
        Инициализация объекта класса PotatoBed.

        :param num_potatoes: Количество картошек на грядке.
        """
        self.potatoes = [Potato(i) for i in range(1, num_potatoes + 1)]

    def grow_potatoes(self):
        """
        Увеличивает стадию зрелости всех картошек на грядке на одну.
        """
        for potato in self.potatoes:
            potato.grow()

    def check_maturity(self):
        """
        Проверяет зрелость всех картошек на грядке.

        :return: True, если все картошки созрели, иначе False.
        """
        for potato in self.potatoes:
            if potato.get_stage() != "Зрелая":
                return False
        return True