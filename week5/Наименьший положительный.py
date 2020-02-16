# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент, а значения всех элементов списка по модулю не превосходят 1000.

listik = list(map(int, input().split()))
minim = 1000
for i in range(len(listik)):
    numb = int(listik[i])
    if numb > 0 and numb < minim:
        minim = numb
print(minim)
