# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.

inp_file = open('input.txt', 'r', encoding='utf8')
outp_file = open('output.txt', 'w', encoding='utf8')

candidates = {}
votes = 0

for line in inp_file:
    cand_name = line.strip()
    candidates[cand_name] = candidates.get(cand_name, 0) + 1
    votes += 1

candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
percent = candidates[0][1] / votes * 100

if percent > 50:
    print(candidates[0][0], file=outp_file)
else:
    for name, vote_amount in candidates[:2]:
        print(name, file=outp_file)

inp_file.close()
outp_file.close()
