# Даны два действительных числа x и y. Проверьте, принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.

def IsPointInSquare(x, y):
    return (-1 <= x <= 1) and (-1 <= y <= 1)


x = float(input())
y = float(input())
print('YES') if IsPointInSquare(x, y) else print('NO')
