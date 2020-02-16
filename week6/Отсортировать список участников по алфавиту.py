# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').

inFile = open('input.txt', 'r', encoding='utf-8')
matrix = []
for line in inFile:
    line = line.split()
    line.pop(2)
    matrix.append(line)
inFile.close()
matrix.sort()
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
