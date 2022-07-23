"""
main program file which will call both oops and functional
programing code, and will show result accordingly
"""
import os
import sys

# inserting current project path to sys path, can be removed
# after setting project path directly in OS
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import oops.main
import functional.main


def get_input(msg: str, start_range: int, end_range: int) -> int:
    """ gets input from the user
    """
    while True:
        input_num = input(msg)
        if input_num.isdigit():
            input_num = int(input_num)
            if end_range >= input_num >= start_range:
                return input_num
        print("Invalid Input, Try again")


if __name__ == '__main__':
    expert = get_input("Enter 1 for expert1, 2 for expert2, and 3 for expert3: ", 1, 3)
    num = get_input("Enter an integer number between 2 to 10: ", 2, 10)
    print("oops script output")
    print(oops.main.calculate(expert, num))
    print("functional script output")
    print(functional.main.calculate(expert, num))
