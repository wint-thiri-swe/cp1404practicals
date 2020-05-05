"""
Github link: https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac06/programming_language.py
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if typing is Dynamic"""
        return self.typing == 'Dynamic'

    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)
