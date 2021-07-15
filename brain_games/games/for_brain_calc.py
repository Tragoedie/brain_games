"""This is the calculator game logic."""
from random import choice, randint

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100
OPERATOR_ADD = '+'
OPERATOR_SUBSTRACT = '-'
OPERATOR_MULTIPLY = '*'


def generate_expression():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    numb_one = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    numb_two = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    string_operator = (OPERATOR_ADD, OPERATOR_SUBSTRACT, OPERATOR_MULTIPLY)
    operator = choice(string_operator)
    if operator == OPERATOR_ADD:
        op_result = numb_one + numb_two
    elif operator == OPERATOR_SUBSTRACT:
        op_result = numb_one - numb_two
    else:
        op_result = numb_one * numb_two
    return '{0} {1} {2}'.format(numb_one, operator, numb_two), str(op_result)
