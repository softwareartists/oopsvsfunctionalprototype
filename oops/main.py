"""Calculate the result as per OOPS implementation"""
import os
from utils import load_yaml
from oops.experts import Experts


def calculate(expert: int, num: int) -> str:
    """Loads data from config as per user input
    and then runs calculate as per expert.
    """
    data = load_yaml.load_yaml(os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.path.join("configs", "expert.yaml")))
    if data.get(expert):
        expert = Experts(**data.get(expert))
        return expert.calculate(num)
    return "Invalid Input"
