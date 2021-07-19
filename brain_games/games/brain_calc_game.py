"""This is the calculator game logic."""
import random

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100
OPERATOR_ADD = '+'
OPERATOR_SUBSTRACT = '-'
OPERATOR_MULTIPLY = '*'


def get_start_game_string():
    """Brain-calc game greeting string.

    Returns:
        basestring: greeting string.
    """
    return 'What is the result of the expression?.'


def get_question_and_correct_answer():
    """Generate question and right answer.

    Returns:
        basestring: returns expression with result.
    """
    number_one = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    number_two = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    operators = (OPERATOR_ADD, OPERATOR_SUBSTRACT, OPERATOR_MULTIPLY)
    operator = random.choice(operators)
    correct_ans = str(get_correct_answer(number_one, number_two, operator))
    return '{0} {1} {2}'.format(number_one, operator, number_two), correct_ans


def get_correct_answer(number_one, number_two, operator):
    """Check if game is finished.

    Parameters:
        number_one (int): number.
        number_two (int): number.
        operator (string): math operator

    Returns:
        basestring: returns correct answer.
    """
    if operator == OPERATOR_ADD:
        return number_one + number_two
    elif operator == OPERATOR_SUBSTRACT:
        return number_one - number_two
    return number_one * number_two
