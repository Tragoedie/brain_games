"""This is the parity game logic."""
from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    get_random_number,
    is_win_or_not,
)


def brain_even_logic():
    """Define even game logic."""
    start_str = 'Answer "yes" if the number is even, otherwise answer "no".'
    name_user, count = ask_user_name_and_greeting(start_str), 0
    while True:
        question = get_random_number()
        user_ans = ask_question_and_get_answer(question)
        corr_ans = is_parity(question)
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


def is_parity(number):
    """Check if number is odd.

    Args:
        number (int): number to check.

    Returns:
        basestring: returns expression with result.
    """
    return 'yes' if number % 2 == 0 else 'no'
