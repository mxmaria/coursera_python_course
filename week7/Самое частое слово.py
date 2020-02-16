# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

with open('input.txt', 'r') as inp_file:
    text = inp_file.read()

word_dict = {}
for word in text.split():
    word_dict[word] = word_dict.get(word, 0) + 1

max_word = max(word_dict.values())
most_frequent = [k for k, v in word_dict.items() if v == max_word]
print(min(most_frequent))
