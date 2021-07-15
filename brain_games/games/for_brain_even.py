"""This is the even game logic."""
from random import randint

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100


def is_parity():
    """Check if number is odd.

    Returns:
        basestring: returns expression with result.
    """
    number = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    return number, 'yes' if number % 2 == 0 else 'no'
