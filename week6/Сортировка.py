# Отсортируйте данный массив, используя встроенную сортировку.

n = int(input())
mylist = list(map(int, input().split()))
mylist.sort(reverse=False)
print(*mylist)
