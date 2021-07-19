"""This is the progression game logic."""
import random

LENGTH_PROGRESSION = 10
LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100
LEFT_BORDER_DIFF = 1
RIGHT_BORDER_DIFF = 10


def get_start_game_string():
    """Brain-progression game greeting string.

    Returns:
        basestring: greeting string.
    """
    return 'What number is missing in the progression?.'


def get_question_and_correct_answer():
    """Generate mathematical progression.

    Returns:
        basestring: returns progression string with result.
    """
    start_number = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    step_progression = random.randint(LEFT_BORDER_DIFF, RIGHT_BORDER_DIFF)
    miss_index = random.randint(LEFT_BORDER_NUMBER, LENGTH_PROGRESSION - 1)
    array_progression = get_progression(
        start_number,
        step_progression,
        LENGTH_PROGRESSION,
    )
    correct_answer = array_progression[miss_index]
    array_progression[miss_index] = '..'
    return ' '.join(array_progression), str(correct_answer)


def get_progression(start_number, step_progression, length_progression):
    """Calculate the formula for a member of a mathematical progression.

    Parameters:
        start_number (int): first number of a mathematical progression.
        step_progression (int): difference of a mathematical progression.
        length_progression (int): length of a mathematical progression.

    Returns:
        array of mathematical progression.
    """
    return [
        str(start_number + step_progression * (numb - 1))
        for numb in range(length_progression)
    ]
