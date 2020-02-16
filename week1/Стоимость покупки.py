# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.

a = int(input())
b = int(input())
quant = int(input())
cost = ((a * 100 + b) * quant)
print(cost // 100, cost % 100)
