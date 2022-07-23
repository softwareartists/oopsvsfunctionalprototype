"""
Contains OOPS implementation
of mathematical functions
"""
import abc


# pylint: disable=fixme

class AbstractCalculation(abc.ABC):
    """Abstract implementation for Calculations"""

    def __init__(self, num: int):
        self.num = num

    @abc.abstractmethod
    def __call__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class IsPrime(AbstractCalculation):
    """Check if num is prime"""

    def __call__(self) -> bool:
        if self.num < 2:
            return False
        for i in range(2, int(self.num ** 0.5) + 1):
            if (self.num % i) == 0:
                return False
        return True

    def __str__(self) -> str:
        if self():
            return f'The number {self.num} is a prime number.'
        return f'The number {self.num} is not a prime number.'


class CalculateFactorial(AbstractCalculation):
    """Calculate factorial of the num"""

    def __call__(self) -> int:
        curr = 1
        for i in range(1, self.num + 1):
            curr *= i
        return curr

    def __str__(self) -> str:
        return f'The factorial of {self.num} is {self()}.'


class GetFibonacci(AbstractCalculation):
    """Provides sequence of first num fibonacci numbers"""

    def __call__(self) -> list:
        if self.num == 0:
            return [0]
        fseries = [0, 1]
        if self.num > 2:
            for i in range(2, self.num):
                fseries.append(fseries[i - 1] + fseries[i - 2])
        return fseries

    def __str__(self) -> str:
        return f'The first {self.num} numbers of the Fibonacci series are {self()}.'


class NotImplement(AbstractCalculation):
    """None object implementation"""

    def __call__(self):
        raise Exception("Not Implemented")

    def __str__(self) -> str:
        return 'This expert is not available please try from 1 - 3.'


calculate_map = {
    # TODO: this can be changed to math_of_interest
    #  sticking to name as per requirement
    'Radford': IsPrime,
    'Matt': CalculateFactorial,
    'Alireza': GetFibonacci
}


def calculate_factory(name: str, *args, **kwargs) -> AbstractCalculation:
    """Factory method (design pattern) to select calculation on runtime"""
    return calculate_map.get(name, NotImplement)(*args, **kwargs)
