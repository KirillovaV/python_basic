"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def my_div(div1: float, div2: float) -> float:
    """
    Функция возврещает частное от деления двух чисел
    :param div1: Делимое (число, float)
    :param div2: Делитель (число, float)
    :return: float
    """
    try:
        return div1 / div2
    except ZeroDivisionError:
        print("Ошибка! Деление на 0!")


while True:
    try:
        dividend = float(input("Введите делимое: "))
        break
    except ValueError:
        continue

while True:
    try:
        divider = float(input("Введите делитель: "))
        break
    except ValueError:
        continue

print("Результат деления:", my_div(dividend, divider))
