from random import randint #вызов рандома

n,m=3,5 #рамки массива
a=[[randint(1, 40) for j in range(m)] for i in range(n)] #генерация массива
print(a) #вывод самого массива

max=a[0][0] #начальное значение максимума
for i in range(n):
    for j in range(m):
        if a[i][j]>max:
            max=a[i][j] #если a больше максимума, то оно и становится максимумом
            b=max/2
print(b) #выводим максимальное число сразу разделённым
