# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.

numb_of_pairs = int(input())
synonyms_pair = dict()

for pair in range(numb_of_pairs):
    first_elem, sec_elem = input().split()
    synonyms_pair[first_elem] = sec_elem
    synonyms_pair[sec_elem] = first_elem

print(synonyms_pair[input()])
