"""
Contains functional implementation
of mathematical functions
"""


# pylint: disable=unnecessary-lambda-assignment, import-outside-toplevel

def is_prime(num: int) -> str:
    """Check if num is prime"""
    fun = lambda x: any(True for i in range(2, int(x ** 0.5) + 1) if x % i == 0)
    if num > 1 and not fun(num):
        return f'The number {num} is a prime number.'
    return f'The number {num} is not a prime number.'


def calculate_factorial(num: int) -> str:
    """Calculate factorial of the num"""
    fun = lambda n: 1 if n == 0 else n * fun(n - 1)
    return f'The factorial of {num} is {fun(num)}.'


def get_fibonacci(num: int) -> str:
    """Provides sequence of first num fibonacci numbers"""
    from functools import reduce
    fun = lambda y: (reduce(lambda x, _: x + (x[-1] + x[-2],),
                            (0 for _ in range(y - 2)), (0, 1))
                     ) if y > 1 else (0,) * y
    return f'The first {num} numbers of the Fibonacci series are {fun(num)}.'
