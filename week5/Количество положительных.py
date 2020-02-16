# Найдите количество положительных элементов в данном списке.

listik = list(map(int, input().split()))
quant = 0
for i in listik:
    if i > 0:
        quant += 1
print(quant)
