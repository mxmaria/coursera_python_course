# Дано действительное положительное число a и целое неотрицательное число n.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).

def power(a, n):
    return a ** n


a = float(input())
n = int(input())

print(power(a, n))
