"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivException(Exception):

    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def is_div_zero(cls, divider):
        if not divider:
            raise cls('Attempt to divide by zero')


if __name__ == '__main__':

    while True:
        try:
            x = float(input("Enter dividend:\n>>>"))
            break
        except ValueError:
            continue
    while True:
        try:
            y = float(input("Enter divisor:\n>>>"))
            MyZeroDivException.is_div_zero(y)
            break
        except ValueError:
            continue
        except MyZeroDivException:
            print("Can't be divided by 0. Enter different number.")

    print(x / y)
