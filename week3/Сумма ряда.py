# По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).

n = float(input())
summ = 0
i = 1
while n >= i:
    s = 1.0 / (i ** 2)
    summ += s
    i += 1
print(summ)
