# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

listik = list(map(int, input().split()))
for i in range(1, len(listik)):
    if int(listik[i]) > int(listik[i - 1]):
        print(listik[i])
