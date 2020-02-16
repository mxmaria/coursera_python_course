# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность порядка корня квадратного из n.

from math import sqrt
n = int(input())


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= sqrt(n):
            print(n)
            return
        i += 1

    print(i)
MinDivisor(n)
