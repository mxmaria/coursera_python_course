# Определите количество четных элементов в последовательности, завершающейся числом 0.

n = int(input())
quant = 0
while n != 0:
    i = n % 2
    if i == 0:
        quant += 1
    n = int(input())
print(quant)
