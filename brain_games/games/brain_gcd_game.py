"""This is the gcd game logic."""
import random

LEFT_BORDER_NUMBER = 0
RIGHT_BORDER_NUMBER = 100


def get_start_game_string():
    """Brain-gcd game greeting string.

    Returns:
        basestring: greeting string.
    """
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_correct_answer():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    number_one = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    number_two = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    question = '{0} {1}'.format(number_one, number_two)
    correct_answer = str(get_gcd_number(number_one, number_two))
    return question, correct_answer


def get_gcd_number(number_one, number_two):
    """Check if game is finished.

    Parameters:
        number_one (int): number.
        number_two (int): number.

    Returns:
        greatest common divisor
    """
    if number_one == 0 or number_two == 0:
        return max(number_one, number_two)
    if number_one > number_two:
        return get_gcd_number(number_one - number_two, number_two)
    return get_gcd_number(number_one, number_two - number_one)
