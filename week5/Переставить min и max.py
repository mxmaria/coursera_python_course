# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.

a = list(map(int, input().split()))
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(*a)
