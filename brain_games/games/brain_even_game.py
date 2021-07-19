"""This is the even game logic."""
import random

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100


def get_start_game_string():
    """Brain-even game greeting string.

    Returns:
        basestring: greeting string.
    """
    return 'Answer "yes" if given number is even. Otherwise answer "no".'


def get_question_and_correct_answer():
    """Generate question and right answer.

    Returns:
        basestring: returns expression with result.
    """
    number = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    return number, 'yes' if number % 2 == 0 else 'no'
