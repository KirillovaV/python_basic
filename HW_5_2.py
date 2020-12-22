"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке.
"""

from os import path

file_path = path.join(path.dirname(__file__), 'TXT', '5_2.txt')
lines_count = 0
words_count = 0

try:
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            lines_count += 1
            line_words_count = len(line.split())
            words_count += line_words_count
            print(f"Строка {lines_count} - количество слов {line_words_count}")
        print(f"Всего в файле {lines_count} строк и {words_count} слов")
except IOError:
    print("Ошибка ввода-вывода")
