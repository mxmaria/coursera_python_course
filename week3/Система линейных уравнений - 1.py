# Даны вещественные числа a, b, c, d, e, f.
# Известно, что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение.
# Выведите два числа x и y, являющиеся решением этой системы.

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if b != 0:
    y = (c * e - a * f) / (b * c - a * d)
    if c != 0:
        x = (f - d * y) / c
        print(x, y)
else:
    if a != 0:
        x = (f * b - d * e) / (b * c - d * a)
        if d != 0:
            y = (f - c * x) / d
            print(x, y)
