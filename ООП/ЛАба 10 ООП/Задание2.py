# Создаем класс MilitaryPersonnel
class MilitaryPersonnel:
    def __init__(self, фамилия, рота, звание, дата_рождения, дата_поступления, часть):
        self.фамилия = фамилия
        self.рота = рота
        self.звание = звание
        self.дата_рождения = дата_рождения
        self.дата_поступления = дата_поступления
        self.часть = часть

    def __str__(self):
        return f"Фамилия: {self.фамилия}, Рота: {self.рота}, Звание: {self.звание}, Дата рождения: {self.дата_рождения}, Дата поступления: {self.дата_поступления}, Часть: {self.часть}"

# Создаем класс MilitaryAdministration, наследующийся от класса MilitaryPersonnel
class MilitaryAdministration(MilitaryPersonnel):
    def __init__(self, фамилия, рота, звание, дата_рождения, дата_поступления, часть, название_округа, должность, выслуга_лет, сумма_надбавки):
        super().__init__(фамилия, рота, звание, дата_рождения, дата_поступления, часть)
        self.название_округа = название_округа
        self.должность = должность
        self.выслуга_лет = выслуга_лет
        self.сумма_надбавки = сумма_надбавки

    def __str__(self):
        return f"{super().__str__()}, Название округа: {self.название_округа}, Должность: {self.должность}, Выслуга лет: {self.выслуга_лет}, Сумма надбавки: {self.сумма_надбавки}"

# Создаем класс ContractMilitaryService, наследующийся от класса MilitaryPersonnel
class ContractMilitaryService(MilitaryPersonnel):
    def __init__(self, фамилия, рота, звание, дата_рождения, дата_поступления, часть, период_договора, дата_договора, номер_протокола, сумма_зарплаты):
        super().__init__(фамилия, рота, звание, дата_рождения, дата_поступления, часть)
        self.период_договора = период_договора
        self.дата_договора = дата_договора
        self.номер_протокола = номер_протокола
        self.сумма_зарплаты = сумма_зарплаты

    def __str__(self):
        return f"{super().__str__()}, Период договора: {self.период_договора}, Дата договора: {self.дата_договора}, Номер протокола: {self.номер_протокола}, Сумма зарплаты: {self.сумма_зарплаты}"

# Создаем класс Awarded, наследующийся от класса MilitaryPersonnel
class Awarded(MilitaryPersonnel):
    def __init__(self, фамилия, рота, звание, дата_рождения, дата_поступления, часть, название_награды, премия, сумма_надбавки):
        super().__init__(фамилия, рота, звание, дата_рождения, дата_поступления, часть)
        self.название_награды = название_награды
        self.премия = премия
        self.сумма_надбавки = сумма_надбавки

    def __str__(self):
        return f"{super().__str__()}, Название награды: {self.название_награды}, Премия: {self.премия}, Сумма надбавки: {self.сумма_надбавки}"

# Создаем экземпляры классов
person1 = MilitaryAdministration("Иванов", "1-я", "прапорщик", "01.01.1980", "01.01.2000", "13-я", "Московский", "начальник", 20, 5000)
person2 = ContractMilitaryService("Петров", "2-я", "сержант", "15.05.1985", "01.01.2010", "27-я", "5 лет", "01.01.2010", 12345, 7000)
person3 = Awarded("Сидоров", "3-я", "лиейтенант", "10.10.1990", "01.01.2015", "40-я", "Орден Мужества", "10000", 2000)

# Выводим информацию об экземплярах классов
print(person1)
print(person2)
print(person3)