# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

prev = -1
curr_rep_len = 0
max_rep_len = 0
n = int(input())
while n != 0:
    if prev == n:
        curr_rep_len += 1
    else:
        prev = n
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    n = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
