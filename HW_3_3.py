"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов
"""


def my_func(arg1, arg2, arg3):
    if type(arg1) == type(arg2) == type(arg3):
        arg_list = [arg1, arg2, arg3]
        arg_list.remove(min(arg_list))
        return arg_list[0] + arg_list[1]
    else:
        print("Невозможно вычислить сумму элементов разных типов.")


print(my_func(6, 2, 9))
