class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса")


car_a = Car()
car_a.vehicle_method()


class Car1:
    def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)
car_a1 = Car1()
car_a1.start(10, 20)



# создание класса Vehicle
class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")


# создание класса, который наследует Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Car")


# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")


# создание класса Vehicle
class Vehicle2:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")


# создание класса, который наследует Vehicle
class Car2(Vehicle2):
    def print_details(self):
        print("Это дочерний метод из класса Car")


# создание класса Cycle, который наследует Vehicle
class Cycle2(Vehicle2):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")

car_a3 = Vehicle2()
car_a3.print_details()

car_b3 = Car2()
car_b3.print_details()

car_c3 = Cycle2()
car_c3.print_details()