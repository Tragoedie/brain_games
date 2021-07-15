"""This is the NOD game logic."""
from math import gcd
from random import randint

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100


def generate_expression():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    number_one = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    number_two = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    return f'{number_one} {number_two}', str(gcd(number_one, number_two))
