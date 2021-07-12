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
    numb_one = get_random_number()
    numb_two = get_random_number()
    operator = random.choice('+-*')
    if operator == '+':
        op_result = numb_one + numb_two
    elif operator == '-':
        op_result = numb_one - numb_two
    else:
        op_result = numb_one * numb_two
    return '{0} {1} {2}'.format(numb_one, operator, numb_two), str(op_result)
