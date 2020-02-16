# Добавьте в предыдущий класс следующие методы:
#
# __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
# __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
# __rmul__, делающий то же самое, что и __mul__.
# Этот метод будет вызван в том случае, аргумент находится справа.
# Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.

from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, list):
        self.list = deepcopy(list)

    def __str__(self):
        rows = []
        for row in self.list:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def __add__(self, mtr):
        rows = deepcopy(self.list)
        for row in range(len(self.list)):
            for i in range(len(self.list[row])):
                rows[row][i] += mtr.list[row][i]
        return Matrix(rows)

    def __mul__(self, n):
        rows = deepcopy(self.list)
        for row in range(len(self.list)):
            for i in range(len(self.list[row])):
                rows[row][i] *= n
        return Matrix(rows)

    def size(self):
        return len(self.list), len(self.list[0])

    __rmul__ = __mul__


exec(stdin.read())
