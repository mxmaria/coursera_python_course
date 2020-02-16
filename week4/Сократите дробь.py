# Сократите дробь (n / m), то есть выведите два других числа p и q таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m и возвращающей кортеж из двух чисел: return p, q

import math

n = int(input())
m = int(input())


def reduce_fraction(n, m):
    k = math.gcd(n, m)
    return (n // k, m // k)

print(*reduce_fraction(n, m))
