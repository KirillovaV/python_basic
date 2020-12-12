"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

product_list = []
count = 0
yes_no_flag = True

product_dict = {
    "наименование": None,
    "цена": None,
    "количество": None,
    "ед.": None
}

print("Введите информацию о товарах.")
while yes_no_flag:
    count += 1
    product_dict["наименование"] = input("Введите наименование: ")
    product_dict["цена"] = input("Введите цену: ")
    product_dict["количество"] = input("Введите количество: ")
    product_dict["ед."] = input("Введите единицы измерения: ")
    product_list.append((count, product_dict.copy()))

    while True:
        yes_no = input("Продолжить ввод? (Да/Нет) ")
        if yes_no.lower() in ("да", "д", "y", "нет", "н", "n"):
            yes_no_flag = yes_no in ("да", "д", "y")
            break
        else:
            continue

for el in product_list:
    print(el)
print("\n")

analytic_dict = {}

for key in product_dict:
    result = []
    for itm in product_list:
        result.append(itm[1][key])
    analytic_dict[key] = result

print(analytic_dict)
