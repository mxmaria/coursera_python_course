Дана последовательность чисел, завершающаяся числом 0.
Найдите сумму всех этих чисел, не используя цикл.

def sum():
    n = int(input())
    if n == 0:
        return 0
    return n + sum()


print(sum())
