"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from os import path

file_path = path.join(path.dirname(__file__), 'TXT', '5_6.txt')
class_hours = {}

try:
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            tmp_line = line.replace('(', ' ').replace(':', ' ').split()
            subject = tmp_line[0]
            hours = 0
            for itm in tmp_line[1:]:
                try:
                    hours += int(itm)
                except ValueError:
                    pass
            class_hours[subject] = hours
except IOError:
    print("Ошибка ввода-вывода")

print(class_hours)
