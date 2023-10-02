from math import*
a=2.6
b=5.1
x = float(input("Введите значение x: "))

if x <= 1:
    y = a * cos(x) ** 2 - b * sin(x ** 2)
elif 1 < x <= 4:
    y = b * log(x) + x ** 3
else: 
    y = sqrt(x ** 2 + a * b)

print("y =", y)

