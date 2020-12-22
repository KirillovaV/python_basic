"""
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
from os import path

firms_dict = {}
average_profit_dict = {}
average_profit = 0
positive_profit_count = 0
firm_list = []

try:
    with open((path.join(path.dirname(__file__), 'TXT', '5_7.txt')), 'r', encoding='UTF-8') as file:
        for line in file:
            firm_data = line.split()
            firm = firm_data[0]
            profit = float(firm_data[2]) - float(firm_data[3])
            firms_dict[firm] = profit

            if profit > 0:
                positive_profit_count += 1
                average_profit += profit

        average_profit = average_profit / positive_profit_count
        average_profit_dict['average_profit'] = average_profit

        firm_list.append(firms_dict)
        firm_list.append(average_profit_dict)

except IOError:
    print("Ошибка ввода-вывода.")

try:
    with open((path.join(path.dirname(__file__), 'TXT', '5_7.json')), 'w', encoding='UTF-8') as file:
        json.dump(firm_list, file)
except IOError:
    print("Ошибка ввода-вывода.")
