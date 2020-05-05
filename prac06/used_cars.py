"""CP1404/CP5632 Practical - Client code to use the Car class.

Github link: https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac06/used_cars.py
"""

from prac06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Ferrari", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("MINI Cooper", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)


if __name__ == '__main__':
    main()
