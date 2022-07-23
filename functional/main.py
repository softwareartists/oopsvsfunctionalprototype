"""Calculate the result as per Functional implementation"""
import os
from utils import load_yaml
from functional.experts import are_panel
from functional.calculation import is_prime
from functional.calculation import calculate_factorial
from functional.calculation import get_fibonacci


def calculate(expert, num):
    """Loads data from config as per user input
    and then runs calculate as per expert.
    """
    data = load_yaml.load_yaml(os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.path.join("configs", "expert.yaml")))
    if data.get(expert):
        if are_panel(**data.get(expert)):
            if expert == 1:
                return is_prime(num)
            if expert == 2:
                return calculate_factorial(num)
            if expert == 3:
                return get_fibonacci(num)
    return "Invalid Input"
