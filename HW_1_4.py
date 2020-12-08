"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_num = input("Введите целое положительное число\n>>>")
while not user_num.isdigit() or int(user_num) == 0:
    user_num = input("Введите целое положительное число\n>>>")
user_num = int(user_num)
biggest_num = 0

while user_num > 0:
    if (user_num % 10) > biggest_num:
        biggest_num = user_num % 10
    user_num = user_num // 10

print("Самая большая цифра в числе", biggest_num)
