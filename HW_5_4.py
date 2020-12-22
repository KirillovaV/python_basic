"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные должнызаменяться
на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

from os import path

en_ru_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

file1_path = path.join(path.dirname(__file__), 'TXT', '5_4_1.txt')
file2_path = path.join(path.dirname(__file__), 'TXT', '5_4_2.txt')
new_lines = []

try:
    with open(file1_path, 'r', encoding='UTF-8') as file:
        for line in file:
            new_lines.append(' '.join((en_ru_dict[line.split(' ')[0]],
                                       *line.split(' ')[1:])))
except IOError:
    print("Ошибка ввода-вывода.")

try:
    with open(file2_path, 'w', encoding='UTF-8') as file:
        file.writelines(new_lines)
except IOError:
    print("Ошибка ввода-вывода.")
