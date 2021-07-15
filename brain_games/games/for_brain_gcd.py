"""This is the NOD game logic."""
from random import randint

LEFT_BORDER_NUMBER = 0
RIGHT_BORDER_NUMBER = 100


def generate_expression():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    number_one = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    number_two = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    return f'{number_one} {number_two}', str(gcd_number(number_one, number_two))


def gcd_number(number_one, number_two):
    """Check if game is finished.

    Parameters:
        number_one (int): number.
        number_two (int): number.

    Returns:
        NOD
    """
    if number_one == 0 or number_two == 0:
        return max(number_one, number_two)
    if number_one > number_two:
        return gcd_number(number_one - number_two, number_two)
    return gcd_number(number_one, number_two - number_one)
