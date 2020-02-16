# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.

import math
percent = float(input())
rub = float(input())
kop = float(input())
money = (rub * 100) + kop
fin_perc = money * (percent / 100)
fin_mon = (money + fin_perc) / 100
fin_rub = math.floor(fin_mon)
fin_kop = int(round((fin_mon - fin_rub) * 100, 2))
print(fin_rub, fin_kop, sep=' ')
