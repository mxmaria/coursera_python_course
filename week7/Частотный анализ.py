# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.

with open('input.txt', 'r') as inp_file:
    text = inp_file.read().split()

word_dict = {}

for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for i in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])
