# По данному натуральному n≤9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.

n = int(input())

for i in range(n):
    for j in range(1, i + 2):
        print(j, end='')
    print()
