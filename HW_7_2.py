"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod
import random


class Clothes(ABC):

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    name = "coat"

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.name} - size {self.size}"

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    name = "suit"

    def __init__(self, height):
        self.height = height

    def __str__(self):
        return f"{self.name} - height {self.height}"

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


class Production(Clothes):
    clothes = []

    def __str__(self):
        result = "Atelier order:\n" + '; '.join(map(str, self.clothes))
        return result

    def add_coats(self, size):
        self.clothes.append(Coat(size))

    def add_suits(self, height):
        self.clothes.append(Suit(height))

    @property
    def fabric_consumption(self):
        result = 0
        for itm in self.clothes:
            result += itm.fabric_consumption
        return result


if __name__ == '__main__':
    coat = Coat(48)
    print(f"For {coat} - {coat.fabric_consumption:.2f}m2 needed")

    suit = Suit(1.60)
    print(f"For {suit} - {suit.fabric_consumption:.2f}m2 needed")

    atelier = Production()
    atelier.clothes = []
    for _ in range(5):
        atelier.add_coats(random.randrange(42, 56, 2))
        atelier.add_suits(random.randint(150, 190) / 100)

    print(atelier)
    print(f"Fabric consumption for order: {atelier.fabric_consumption:.2f}m2")
