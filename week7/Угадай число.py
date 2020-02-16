# Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август.
# Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
# Наконец, последняя строка входных данных содержит одно слово HELP.
# Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.

n = int(input())
our_set = set(range(1, n + 1))
while True:
    question = input()
    if question == 'HELP':
        break
    question = {int(x) for x in question.split()}
    answer = input()
    if answer == 'YES':
        our_set &= question
    if answer == 'NO':
        our_set -= question
print(' '.join([str(x) for x in sorted(our_set)]))
