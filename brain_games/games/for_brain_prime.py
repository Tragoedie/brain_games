"""This is the prime game logic."""

from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    get_random_number,
    is_win_or_not,
)


def brain_prime_logic():
    """Define prime game logic."""
    name_user = ask_user_name_and_greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while True:
        question = get_random_number()
        user_ans = ask_question_and_get_answer(question)
        corr_ans = is_prime(question)
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


def is_prime(number):
    """Check if number is prime.

    Args:
        number (int): number to check.

    Returns:
        basestring: returns expression with result.
    """
    return 'yes' if all(number % i for i in range(2, number)) else 'no'
