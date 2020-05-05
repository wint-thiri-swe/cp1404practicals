
class Guitar:
    """Represents a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of guitar by subtracting year input from 2020"""
        return 2020 - self.year

    def is_vintage(self):
        """Return true if the age from get_age is greater than 50"""
        return self.get_age() >= 50
