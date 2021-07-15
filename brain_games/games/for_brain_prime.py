"""This is the prime game logic."""
from random import randint

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100


def is_prime():
    """Check if number is prime.

    Returns:
        basestring: returns expression with result.
    """
    number = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    if number % 2 == 0 or number == 1:
        return number, 'no'
    step = 3
    while step * step <= number and number % step != 0:
        step += 2
    return number, 'yes' if step * step > number else 'no'
