"""This is the NOD game logic."""
from math import gcd

from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    get_random_number,
    is_win_or_not,
)


def brain_gcd_logic():
    """Define NOD game logic."""
    name_user = ask_user_name_and_greeting()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while True:
        question, corr_ans = generate_expression()
        user_ans = ask_question_and_get_answer(question)
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


def generate_expression():
    """Generate mathematical expression.

    Returns:
        basestring: returns expression with result.
    """
    number_one = get_random_number()
    number_two = get_random_number()
    return f'{number_one} {number_two}', str(gcd(number_one, number_two))
