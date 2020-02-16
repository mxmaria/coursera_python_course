# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

n = int(input())
max_el = n
quant_of_el = 0
while n != 0:
    if n > max_el:
        max_el = n
        quant_of_el = 1
    elif n == max_el:
        quant_of_el += 1
    n = int(input())
print(quant_of_el)
