"""This is the progression game logic."""

from brain_games.games.engine import brain_game_logic, get_random_number


def brain_progression_logic():
    """Define progression game logic."""
    start_str = 'What number is missing in the progression?.'
    brain_game_logic(start_str, generate_progression)


def generate_progression():
    """Generate mathematical progression.

    Returns:
        basestring: returns progression string with result.
    """
    number = get_random_number()
    length_prog = 10
    difference_of_progress = get_random_number(left_border=1, right_border=10)
    miss_index = get_random_number(left_border=0, right_border=length_prog - 1)
    corr_answer = 0
    array_progression = []
    for numb in range(length_prog):
        if numb == miss_index:
            array_progression.append('..')
            corr_answer = str(number)
        else:
            array_progression.append(str(number))
        number += difference_of_progress
    return ' '.join(array_progression), corr_answer
