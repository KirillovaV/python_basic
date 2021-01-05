"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""
# никогда не хватало фантазии на такие задания...

from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime
from os import path


# класс-исключение для проверки типа элементов, добавляемых на склад
class EquipmentTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def type_check(cls, item):
        if isinstance(item, (Printer, Scanner, Phone, Notebook)):
            return item
        else:
            raise cls("Invalid type.")


# декоратор, записывает в файл передачу предметов на склад и со склада
def storage_log(function):

    def wrapper(*args):
        function(*args)
        now = datetime.now().strftime('%d.%m.%y %H:%M:%S')

        if len(args) == 3:
            line = f">>> {now} Added to storage '{args[1].name}' in amount {args[2]} items.\n"
        elif len(args) == 4:
            line = f"<<<{now} Moved from storage '{args[2]}' in amount {args[3]} items.\n"

        try:
            with open(path.join(path.dirname(__file__), "log.txt"), "a", encoding="utf-8") as file:
                file.write(line)
        except IOError as e:
            print(e)

    return wrapper


class OfficeEquipmentStorage:
    __storage = defaultdict(list)

    # добавляет технику на склад
    @storage_log
    def to_storage(self, item, count: int):
        if not isinstance(count, int):
            raise ValueError("Count must be 'int' type")
        if EquipmentTypeError.type_check(item):
            self.__storage[item.eq_type].append([item, count])

    # выводит информацию о технике на складе
    # без параметров - о всей технике
    # с параметром - о технике конкретного типа
    def get_info(self, eq_type=None):

        def item_info(item_line):
            itm_count = 0
            for itm in item_line:
                itm_count += itm[1]
                print(f"{itm[0]} - {itm[1]} items", end=', ')
            print(f"\nItems count: {itm_count}.\n")
            return count

        count = 0
        if not eq_type:
            for el in self.__storage:
                print(f"{el}:")
                count += item_info(self.__storage[el])
            print(f"Total items: {count}.")

        elif eq_type in self.__storage.keys():
            item_info(self.__storage[eq_type])

        else:
            print(f"There are no items of the specified type.\n"
                  f"Use one of the following types: {tuple(self.__storage.keys())}")

    # списывает технику со склада
    @storage_log
    def from_storage(self, eq_type: str, name: str, count: int):

        if not isinstance(count, int):
            raise ValueError("Count must be 'int' type")

        # проверяем, есть ли такой тип техники на складе
        if eq_type in self.__storage.keys():
            # записываем количество видов такой техники
            itm_count = len(self.__storage[eq_type])
            for itm in self.__storage[eq_type]:

                # ищем есть ли такое наименование в данном типе
                if itm[0].name == name:
                    if itm[1] > count:
                        itm[1] -= count
                        print(f"{count} items was moved from storage")
                        break
                    # если найдено больше необходимого, уменьшаем количество данного наименования
                    # и прекращаем поиск

                    elif itm[1] == count:
                        self.__storage[eq_type].pop(self.__storage[eq_type].index(itm))
                        break
                    # если найдено достаточно, удаляем элемент полностью

                    else:
                        print(f"Not enough items. Was moved: {itm[1]}, not enough: {count - itm[1]}")
                        self.__storage[eq_type].pop(self.__storage[eq_type].index(itm))
                        break
                    # если найдено, но недостаточно, удаляем элемент и
                    # выдаём сообщение о нехватке техники

                itm_count -= 1
            # Если элементов с таким именем нет в данном типе техники,
            # выводим соответствующее сообщение
            if not itm_count:
                print("There are no items with such name.")
        else:
            print("There are no items of the specified type.")


class OfficeEquipment(ABC):

    @abstractmethod
    def __init__(self, name, year, eq_type):
        if not isinstance(year, int):
            raise ValueError("Year must be 'int' type")
        self.name = name
        self.year = year
        self.eq_type = eq_type

    def __str__(self):
        return f"{self.name} - {self.year}"

    @property
    @abstractmethod
    def get_full_info(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, name: str, year: int,
                 print_type: str, paper_size: str, is_color: bool):
        super().__init__(name, year, "Printers")
        self.print_type = print_type
        self.paper_size = paper_size
        self.is_color = is_color

    @property
    def get_full_info(self):
        return (f"Name: {self.name}\nYear: {self.year}\n"
                f"Print type: {self.print_type}\n"
                f"Paper size: {self.paper_size}\nColor print: {self.is_color}")


class Scanner(OfficeEquipment):

    def __init__(self, name: str, year: int, paper_size: str, dpi: str):
        super().__init__(name, year, "Scanners")
        self.paper_size = paper_size
        self.dpi = dpi

    @property
    def get_full_info(self):
        return (f"{self.eq_type}\nName: {self.name}\n" 
                f"Year: {self.year}\nPaper size: {self.paper_size}\n"
                f"Scan resolution, dpi: {self.dpi}")


class Phone(OfficeEquipment):

    def __init__(self, name: str, year: int, is_fax: bool):
        super().__init__(name, year, "Phones")
        self.is_fax = is_fax

    @property
    def get_full_info(self):
        return f"Name: {self.name}\nYear: {self.year}\nFax: {self.is_fax}\n"


class Notebook(OfficeEquipment):

    def __init__(self, name: str, year: int, screen_diagonal: float):
        super().__init__(name, year, "Notebooks")
        self.diagonal = screen_diagonal

    @property
    def get_full_info(self):
        return f"Name: {self.name}\nYear: {self.year}\nScreen diagonal: {self.diagonal}\n"


if __name__ == "__main__":

    firm_storage = OfficeEquipmentStorage()
    try:
        p1 = Printer("print1",  2000, "Laser", "A4", False)
        p2 = Printer("print2", 2019, "Ink jet", "A4", True)
        s1 = Scanner("scan1", 2015, "A4", "2400x2400")
        t1 = Phone('tel1', 2020, False)
        t2 = Phone('tel2', 2010, True)
        n1 = Notebook("nb1", 2018, 15.6)
    except ValueError as e:
        print(e)

    try:
        firm_storage.to_storage(p1, 4)
        firm_storage.to_storage(p2, 3)
        firm_storage.to_storage(s1, 3)
        firm_storage.to_storage(t1, 6)
        firm_storage.to_storage(t2, 2)
        firm_storage.to_storage(n1, 5)
    except EquipmentTypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    print(p1.get_full_info)

    firm_storage.get_info()
    firm_storage.get_info("Phones")

    try:
        firm_storage.from_storage("Phones", "tel1", 4)
    except ValueError or TypeError as e:
        print(e)

    firm_storage.get_info("Phones")
