from prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes flagfall costs."""
    flagfall = 4.50  # class variable shared across SilverServiceTaxi object

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * self.price_per_km

    def get_fare(self):
        """Return total fare with flagfall added"""
        total = super().get_fare()
        total += self.flagfall
        return total

    def __str__(self):
        """Return a string like a Taxi but with extra fare added."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
