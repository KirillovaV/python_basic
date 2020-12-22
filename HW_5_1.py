"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

from os import path

file_path = path.join(path.dirname(__file__), 'TXT', '5_1.txt')

print("Введите строки для записи. Для завершения ввода введите пустую строку.")
try:
    with open(file_path, 'w', encoding='UTF-8') as file:
        while True:
            user_data = input(">>> ")
            if not user_data:
                break
            file.write(user_data + "\n")
except IOError:
    print("Ошибка ввода-вывода.")
