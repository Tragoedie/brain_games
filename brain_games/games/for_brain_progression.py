"""This is the progression game logic."""

from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    get_random_number,
    is_win_or_not,
)


def brain_progression_logic():
    """Define progression game logic."""
    start_str = 'What number is missing in the progression?.'
    name_user, count = ask_user_name_and_greeting(start_str), 0
    while True:
        question, corr_ans = generate_progression()
        user_ans = ask_question_and_get_answer(question)
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


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
