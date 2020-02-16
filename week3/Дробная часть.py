# Дано положительное действительное число X. Выведите его дробную часть.


import math
n = float(input())
i = math.floor(n)
part = n - i
print(part)
