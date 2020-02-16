# Определите сумму всех элементов последовательности, завершающейся числом 0.

n = int(input())
summ = 0
while n != 0:
    summ += n
    n = int(input())
print(summ)
