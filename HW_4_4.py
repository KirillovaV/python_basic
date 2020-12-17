"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

from random import randint

num_list = [randint(0, 10) for i in range(0, 20)]
print(f"Исходный список:\n{num_list}")

new_list = [el for el in num_list if num_list.count(el) == 1]
print(f"Элементы, не имеющие повторений:\n{new_list}")
