# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

input_file = open('input.txt')
words = input_file.read().split()
word_dict = dict()

for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 0
    print(word_dict[word])
