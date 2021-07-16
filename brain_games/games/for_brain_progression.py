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
    step = randint(LEFT_BORDER_DIFF, RIGHT_BORDER_DIFF)
    miss_index = randint(LEFT_BORDER_NUMBER, LENGTH_PROGR - 1)
    array = [str(number + step * (numb - 1)) for numb in range(LENGTH_PROGR)]
    array[miss_index] = '..'
    corr_ans = get_cor_ans(number, step, miss_index)
    return ' '.join(array), str(corr_ans)


def get_cor_ans(start, step, number):
    """Calculate the formula for a member of a mathematical progression.

    Parameters:
        start (int): first number of a mathematical progression.
        step (int): difference of a mathematical progression.
        number (int): number n-member of a mathematical progression.

    Returns:
        n-member of a mathematical progression.
    """
    return start + step * (number - 1)
