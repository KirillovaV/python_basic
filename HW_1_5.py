"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
"""

income = input("Введите выручку фирмы:\n>>>")
while not income.replace(".", "", 1).isdigit():
    income = input("Введите выручку фирмы:\n>>>")
income = float(income)

expenses = input("Введите издержки фирмы:\n>>>")
while not expenses.replace(".", "", 1).isdigit():
    expenses = input("Введите издержки фирмы:\n>>>")
expenses = float(expenses)

if income < expenses:
    print("Фирма работает с убытком")
elif income == expenses:
    print("Выручка равна издержкам. Прибыли нет.")
else:
    profit = income - expenses
    print(f"Предприятие работает с прибылью {profit:.2f}")
    efficiency = profit / income
    print(f"Рентабельность выручки равна {efficiency:.2f}")
    workers_num = input("Введите количество сотрудников:\n>>>")
    if not workers_num.isdigit() or int(workers_num) == 0:
        print("Невозможно вычислить прибыль в расчете на сотрудника")
    else:
        workers_num = int(workers_num)
        profit_worker = profit / workers_num
        print(f"Прибыль фирмы в расчете на одного сотрудника {profit_worker:.2f}")
