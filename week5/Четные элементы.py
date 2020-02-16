# Выведите все четные элементы списка.

list1 = list(map(int, input().split()))
for i in list1:
    if i % 2 == 0:
        print(i)
