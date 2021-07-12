"""This is the calculator game logic."""
import random

from brain_games.games.engine import brain_game_logic, get_random_number


def brain_calc_logic():
    """Define calculator game logic."""
    start_str = 'What is the result of the expression?.'
    brain_game_logic(start_str, generate_expression)


def generate_expression():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    number_one = get_random_number()
    number_two = get_random_number()
    operator = random.choice('+-*')
    if operator == '+':
        expression_result = number_one + number_two
    elif operator == '-':
        expression_result = number_one - number_two
    else:
        expression_result = number_one * number_two
    return f'{number_one} {operator} {number_two}', str(expression_result)
