import random
from prac08.car import Car


class UnreliableCar(Car):
    """Specialised version of Car that include reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car, based on reliability"""
        number = random.randint(0, 100)
        if number > self.reliability:
            distance = 0
        driven_distance = super().drive(distance)
        return driven_distance
