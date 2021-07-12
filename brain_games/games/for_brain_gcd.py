"""This is the NOD game logic."""
from math import gcd

from brain_games.games.engine import brain_game_logic, get_random_number


def brain_gcd_logic():
    """Define NOD game logic."""
    start_str = 'Find the greatest common divisor of given numbers.'
    brain_game_logic(start_str, generate_expression)


def generate_expression():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    number_one = get_random_number()
    number_two = get_random_number()
    return f'{number_one} {number_two}', str(gcd(number_one, number_two))
