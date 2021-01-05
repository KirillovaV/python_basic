"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime


class StringDate:

    def __init__(self, date_str: str):
        """
        :param date_str: Expected date format: "dd-mm-yyyy"
        """
        self.date_str = date_str

    @classmethod
    def str_to_date(cls, date_str):
        try:
            day, mon, year = map(int, date_str.split('-'))
        except ValueError:
            print("Invalid date format")
            return 0, 0, 0
        return day, mon, year

    @staticmethod
    def validation(date_str):
        if not StringDate.str_to_date(date_str):
            print("Invalid date format")
        else:
            day, mon, year = StringDate.str_to_date(date_str)
            max_day = 31

            if not 1900 <= year <= datetime.datetime.now().year:
                print("Year out of range")
            else:
                print("Year is valid")

            if not 1 <= mon <= 12:
                print("Month out of range")
            else:
                print("Month is valid")
                if mon == 2:
                    max_day = 29
                elif mon in (4, 6, 9, 11):
                    max_day = 30

            if not 1 <= day <= max_day:
                print("Day out of range")
            else:
                print("Day is valid")


if __name__ == '__main__':
    print(StringDate.str_to_date('30-02-2020'))
    StringDate.validation('15-02-2022')
    StringDate.validation('32-15-2020')
    StringDate.validation('dd-mm-yyyy')
