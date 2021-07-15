"""This is the progression game logic."""
from random import randint

LENGTH_PROGR = 10
LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100
LEFT_BORDER_DIFF = 1
RIGHT_BORDER_DIFF = 10


def generate_progression():
    """Generate mathematical progression.

    Returns:
        basestring: returns progression string with result.
    """
    start_number = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    difference_of_progress = randint(LEFT_BORDER_DIFF, RIGHT_BORDER_DIFF)
    miss_index = randint(LEFT_BORDER_NUMBER, LENGTH_PROGR - 1)
    array_progression = []
    number = start_number
    for numb in range(LENGTH_PROGR):
        if numb == miss_index:
            array_progression.append('..')
        else:
            array_progression.append(str(number))
        number += difference_of_progress
    corr_answer = get_correct_answer(start_number, difference_of_progress, miss_index)
    return ' '.join(array_progression), str(corr_answer)


def get_correct_answer(start, step, number):
    """Calculate the formula for a member of a mathematical progression.

    Parameters:
        start (int): first number of a mathematical progression.
        step (int): difference of a mathematical progression.
        number (int): number n-member of a mathematical progression.

    Returns:
        n-member of a mathematical progression.
    """
    return start + step * (number - 1)
