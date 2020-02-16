# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².

n = int(input())
summ = 0
i = 1
while i <= n:
    summ += i ** 2
    i += 1
print(summ)
