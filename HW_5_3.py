"""
3. Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from os import path

file_path = path.join(path.dirname(__file__), 'TXT', '5_3.txt')
workers_count = 0
workers_payment = 0

try:
    with open(file_path, 'r', encoding='UTF-8') as file:
        print("Сотрудники с окладом меньше 20 тысяч:")
        for line in file:
            workers_count += 1
            worker = line.split()
            workers_payment += float(worker[1])
            if float(worker[1]) < 20000:
                print(worker[0])
    print(f"Средняя заработная плата всех сотрудников: {workers_payment / workers_count:.2f}")
except IOError:
    print("Ошибка ввода вывода.")
