"""
Contains Expert Implementation as per OOPS
"""
from oops.calculation import calculate_factory


# pylint: disable=R0913, R0903

class Experts:
    """Expert Detail object"""

    def __init__(self, name: str, company: str, discipline: str,
                 position: str, math_of_interest: str):
        self.name = name
        self.company = company
        self.discipline = discipline
        self.position = position
        self.math_of_interest = math_of_interest

    def calculate(self, num: int) -> str:
        """Calculate the value as per Expert"""
        cal_obj = calculate_factory(self.name, num)
        return cal_obj
