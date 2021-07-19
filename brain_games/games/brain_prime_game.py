"""This is the prime game logic."""
import random

LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100


def get_start_game_string():
    """Brain-prime game greeting string.

    Returns:
        basestring: greeting string.
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_correct_answer():
    """Check if number is prime.

    Returns:
        basestring: returns expression with result.
    """
    number = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    return number, is_prime(number)


def is_prime(number):
    """Check if number is prime.

    Parameters:
        number (int): number.

    Returns:
        basestring: returns correct answer.
    """
    if number % 2 == 0 or number == 1:
        return 'no'
    step = 3
    while step * step <= number and number % step != 0:
        step += 2
    return 'yes' if step * step > number else 'no'
