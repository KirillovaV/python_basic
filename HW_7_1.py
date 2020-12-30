"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""
from typing import List


class Matrix:

    def __init__(self, lines: List[list]):

        if not isinstance(lines, list):
            raise ValueError("List[list] expected")

        for itm in lines:
            if not isinstance(itm, list):
                raise ValueError("List[list] expected")

        width = len(lines[0])
        for itm in lines[1:]:
            if width != len(itm):
                raise ValueError("Matrix strings is not equal")

        self.__lines = lines
        self.__height = len(lines)
        self.__width = len(lines[0])

    def __str__(self):
        max_len = 0
        for line in self.__lines:
            for itm in line:
                if max_len < len(str(itm)):
                    max_len = len(str(itm))

        result = ''
        for line in self.__lines:
            result += "".join(f"{itm:^{max_len+1}}" for itm in line) + "\n"
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Added element is not a matrix")
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Not equal size Matrix")

        result = [[(self.__lines[i][j] + other.__lines[i][j]) for j in range(self.__width)]
                  for i in range(self.__height)]

        return Matrix(result)


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(m1)

    m2 = Matrix([[11, 22, 33], [44, 55, 66]])
    print(m2)

    m3 = m1 + m2
    print(m3)
