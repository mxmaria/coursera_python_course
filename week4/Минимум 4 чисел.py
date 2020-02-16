# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел, которая не содержит инструкции if,
# а использует стандартную функцию min от двух чисел.
# Считайте четыре целых числа и выведите их минимум.

a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b, c, d):
    minimum = min(d, min(c, min(a, b)))
    return minimum

print(min4(a, b, c, d))
