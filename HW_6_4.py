"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

import random


class Car:

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction: str):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч.")


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч.")
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч.")
        if self.speed < 30:
            print("Плетемся, как черепаха!")
        elif self.speed > 100:
            print("Вот это скорость!")


class WorkCar(Car):

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч.")
        if self.speed > 45:
            print("Превышение скорости!")


class PoliceCar(Car):

    def __init__(self, speed: float, name: str):
        self.speed = speed
        self.name = name
        super().__init__(speed, "White & Blue", name, True)


def car_movement(car):
    directions = ("на лево.", "на право.", "на дачу.", "в пропасть!")

    car.go()
    print(f"Цвет машины {car.color}")
    car.speed = random.randint(20, 200)
    car.turn(random.choice(directions))
    car.show_speed()
    car.stop()
    print("Приехали!\n")


town_car = TownCar(50, "Gray", "Ford Focus")
sport_car = SportCar(190, "Silver", "Jaguar")
work_car = WorkCar(30, "Yellow", "Taxi", False)
police_car = PoliceCar(90, "Police")

car_movement(town_car)
car_movement(sport_car)
car_movement(work_car)
car_movement(police_car)
