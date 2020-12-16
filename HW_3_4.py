"""
4. Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение числа x
в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""


# Решение через **
def my_func_1(x, y):
    return 1 / x ** abs(y)


# Решение через цикл
def my_func_2(x: float, y: int) -> float:
    """
    Функция для возведения действительных чисей в отрицательную степень
    :param x: Число - основание степени
    :param y: Целое отрицательное число - сеппень
    :return: х в степени у
    """
    result = x
    for i in range(1, abs(y)):
        result *= x
    result = 1 / result
    return result


while True:
    try:
        base = float(input("Введите действительное положительное число (основание)\nx = "))
        if base > 0:
            break
        else:
            continue
    except ValueError:
        continue

while True:
    try:
        degree = int(input("Введите целое отрицательное число (степень)\ny = "))
        if degree < 0:
            break
        else:
            continue
    except ValueError:
        continue


print(pow(base, degree))  # проверка

print(my_func_1(base, degree))
print(my_func_2(base, degree))
