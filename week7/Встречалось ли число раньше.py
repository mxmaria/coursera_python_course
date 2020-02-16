# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

given_list = list(map(int, input().split()))
new_set = set()
for element in given_list:
    if element in new_set:
        print('YES')
    else:
        print('NO')
        new_set.add(element)
