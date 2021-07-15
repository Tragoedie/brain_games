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
    number = randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    difference_of_progress = randint(LEFT_BORDER_DIFF, RIGHT_BORDER_DIFF)
    miss_index = randint(LEFT_BORDER_NUMBER, LENGTH_PROGR - 1)
    corr_answer = 0
    array_progression = []
    for numb in range(LENGTH_PROGR):
        if numb == miss_index:
            array_progression.append('..')
            corr_answer = str(number)
        else:
            array_progression.append(str(number))
        number += difference_of_progress
    return ' '.join(array_progression), corr_answer
