# 1.	Создайте  модель из жизни. Это может быть бронирование комнаты в отеле, покупка билета в транспортной
# компании, или простая РПГ. Создайте несколько объектов классов, которые описывают ситуацию. Объекты должны
# содержать как атрибуты так и методы класса для симуляции различных действий. Программа должна инстанцировать
# объекты и эмулировать какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.

# ===================================================================
### Ооочень круто, что сделал модельку, приближенную к теме своего проекта
### Мне кажется, для твоего проекта - тут готовый калькулятор расхода автомобиля, может дополнить еще что-то
class Car:
    """Родитель для автомобилей"""

    def __init__(self, make: str, model: str, year: int, color: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self) -> None:  # Ускорение
        self.speed += 10

    def brake(self) -> None:  # Торможение
        if self.speed >= 10:
            self.speed -= 10

    def get_speed(self) -> int:  # Ехать, тратя топлива
        return self.speed


class ElectricCar(Car):
    """Электроавтомобиль"""

    def __init__(self, make: str, model: str, year: int, color: str, battery_size: int):
        super().__init__(make, model, year, color)
        self.battery_size = battery_size
        self.charge_level = 100

    def charge_battery(self) -> None:  # Зарядка
        if self.charge_level < 100:
            self.charge_level += 10
            print(f"{self.make} {self.model} {self.year} is charging")
            print(f"Current charge level: {self.charge_level}")

    def drive(self) -> None:  # Ехать, тратя топлива
        if self.charge_level >= 10:
            print(f"{self.make} {self.model} {self.year} is driving")
            self.charge_level -= 10
            self.accelerate()
            print(f"Current speed: {self.get_speed()} kph")
            print(f"Current charge level: {self.charge_level} %")
        else:
            print(f"{self.make} {self.model} {self.year} battery is too low to drive.")


class GasCar(Car):
    """Атомобиль на топливе (дизель или бензин)"""

    def __init__(self, make, model, year, color, fuel_capacity):
        super().__init__(make, model, year, color)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity

    def refuel(self) -> None:  # Заправка
        if self.fuel_level < self.fuel_capacity:
            self.fuel_level += 10
            print(f"{self.make} {self.model} {self.year} is refueling")
            print(f"Current fuel level: {self.fuel_level}")

    def drive(self) -> None:  # Ехать, тратя топлива
        if self.fuel_level >= 1:
            print(f"{self.make} {self.model} {self.year} is driving")
            self.fuel_level -= 1
            self.accelerate()
            print(f"Current speed: {self.get_speed()} kph")
            print(f"Current fuel level: {self.fuel_level}")
        else:
            print(f"{self.make} {self.model} {self.year} is out of gas")


class FuelStation:
    """Заппрвка для электромобилей и авто с жидким топливом"""

    def __init__(self):
        self.gas_cars = []
        self.electric_cars = []

    def add_car(self, car) -> None:
        if isinstance(car, GasCar):
            self.gas_cars.append(car)
            print(f"{car.make} {car.model} {car.year} added to gas station")
        elif isinstance(car, ElectricCar):
            self.electric_cars.append(car)
            print(f"{car.make} {car.model} {car.year} added to electric station")
        else:
            print(f"{car.make} {car.model} {car.year} is not a gas or electric car")

    def refuel_cars(self) -> None:
        for car in self.gas_cars:
            car.refuel()

    def charge_cars(self) -> None:
        for car in self.electric_cars:
            car.charge_battery()


# Пару примеров использования реализованных задач

# fuel_station = FuelStation()
# my_electric_car = ElectricCar("Tesla", "Model S Plaid", "2022", "Red", 100)
# my_gas_car = GasCar("Porsche", "911 Turbo S", "2022", "Purple", 60)
# my_gas_car_2 = GasCar("Toyota", "Supra", 2021, "Red", 80)
# my_gas_car_3 = GasCar("Renault", "Twingo", 2007, "White", 50)
#
# fuel_station.add_car(my_electric_car)
# fuel_station.add_car(my_gas_car)
#
# my_electric_car.drive()
# my_electric_car.charge_battery()
# my_electric_car.drive()
#
# my_gas_car.drive()
# my_gas_car.refuel()
# my_gas_car.drive()
#
# fuel_station.refuel_cars()
# ===================================================================


# 2.	Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений (но не
# более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено исключение типа
# TooManyErrors


# ===================================================================
class TooManyErrors(Exception):  # Если я правильно понял, то нужно было создать свою ошибку  #Правильно
    pass


def repeat(n: int) -> None:
    def dec(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func()  # Возвращаю, если нет ошибок
                except Exception as e:
                    print(f"Error {i + 1}: {e}")
            raise TooManyErrors(f"Too Many Errors - {n}")

        return wrapper

    return dec


# @dec
@repeat(11)
def task_2() -> str:
    import random
    choose = random.choice([Exception, "ok", Exception, Exception])
    if choose == Exception:
        print("NOOOOO")
        raise Exception
    else:
        print("Nice")
        return "Good"


task_2()


# ===================================================================

# 3.	Выберите себе задачу по ссылке: https://euler.jakumo.org/problems/pg/1.html Решите ее в виде функции и
# покройте тестами. Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится
# ‘assertRaises’.


# Задача 28
# Диагонали числовой спирали
# Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# Можно убедиться, что сумма чисел в диагоналях равна 101.
#
# Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?

# ===================================================================
def number_spiral_diagonals(n: int) -> int | bool:  # n - это колличество строк и столбцов матрицы
    """Только для квадратной матрицы, так как по условиям были квадратные"""
    if n == 1:
        # для единичной матрицы
        return 1
    else:
        try:
            answer = 1
            # Не очень нравится односточный вариант, но решил попрактиковать
            answer += sum(4 * i * i - 6 * (i - 1) for i in range(3, n + 1, 2))
            return answer
        except TypeError:
            return False
# print(number_spiral_diagonals("5"))
# ===================================================================
# все супер, одна строка и правда не супер-читаемая, но все правильно
