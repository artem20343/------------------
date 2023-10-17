<<<<<<< HEAD
# Импортируем класс PotatoBed из модуля potato_bed
from potato_bed import PotatoBed

# Создаем объект класса PotatoBed с 5 грядками
potato_bed = PotatoBed(5)

# Выращиваем картошку на каждой грядке
for _ in range(3):
    potato_bed.grow_potatoes()
    
    # Выводим информацию о каждой картошке
    for potato in potato_bed.potatoes:
        print(f"Картошка {potato.number} сейчас {potato.get_stage()}")
    
    # Проверяем, все ли картошки созрели
    if potato_bed.check_maturity():
        print("Вся картошка созрела. Можно собирать!")
    else:
        print("Картошка ещё не созрела!")
    
=======
# Импортируем класс PotatoBed из модуля potato_bed
from potato_bed import PotatoBed

# Создаем объект класса PotatoBed с 5 грядками
potato_bed = PotatoBed(5)

# Выращиваем картошку на каждой грядке
for _ in range(3):
    potato_bed.grow_potatoes()
    
    # Выводим информацию о каждой картошке
    for potato in potato_bed.potatoes:
        print(f"Картошка {potato.number} сейчас {potato.get_stage()}")
    
    # Проверяем, все ли картошки созрели
    if potato_bed.check_maturity():
        print("Вся картошка созрела. Можно собирать!")
    else:
        print("Картошка ещё не созрела!")
    
>>>>>>> ed71ffae37781bd81cd840534a288057e66a6392
    print()