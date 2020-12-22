"""
5. Создать (программно) текстовый файл, записать в него
программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from os import path
from random import randint

file_path = path.join(path.dirname(__file__), 'TXT', '5_5.txt')

# Создаём файл, записываем в него 10 случайных чисел
try:
    with open(file_path, 'w', encoding='UTF-8') as file:
        for _ in range(10):
            file.write(str(randint(1, 10)) + ' ')
except IOError:
    print("Ошибка ввода-вывода.")

# Читаем числа из файла и подсчитываем сумму
try:
    with open(file_path, 'r', encoding='UTF-8') as file:
        numbers = list(map(int, file.read().split()))
    print(numbers)
    print(sum(numbers))
except IOError:
    print("Ошибка ввода-вывода.")
