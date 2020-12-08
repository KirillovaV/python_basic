"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

int_var = 5
float_var = 3.6
str_var = "some text"

print(f"Объявлены переменные {int_var =}, {float_var =}, {str_var =}")

user_int = input("Введите целое число: ")
if user_int.isdigit():
    user_int = int(user_int)
else:
    print("Введено не целое число.")
user_float = input("Введите дробное число: ")
if user_float.replace(".", "", 1).isdigit():
    user_float = float(user_float)
else:
    print("Введено не число.")
user_str = input("Введите текст: ")

print("Вы ввели:", user_int, user_float, user_str)
