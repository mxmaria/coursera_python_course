# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.

import math
a = float(input())
b = float(input())
c = float(input())
discr = b ** 2 - 4 * a * c
while a != 0:
    if discr > 0:
        x1 = (-b - math.sqrt(discr)) / (2 * a)
        x2 = (-b + math.sqrt(discr)) / (2 * a)
        if x1 > x2:
            print(x2, x1, sep=' ')
        elif x1 < x2:
            print(x1, x2, sep=' ')
        break
    if discr == 0:
        x1 = (-b - math.sqrt(discr)) / (2 * a)
        print(x1)
        break
    if discr < 0:
        break
