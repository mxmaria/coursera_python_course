# Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.

n = int(input())
mass_elems = list(map(int, input().split()))
diff_from_number = int(input())

min_diff_elem = mass_elems[0]

min_diff = abs(min_diff_elem - diff_from_number)

for elem in mass_elems:
    current_diff = abs(diff_from_number - elem)
    if current_diff < min_diff:
        min_diff = current_diff
        min_diff_elem = elem

print(min_diff_elem)
