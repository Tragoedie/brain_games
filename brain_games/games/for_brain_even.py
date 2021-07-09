import random

from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    is_win_or_not,
)


def brain_even_logic():
    name_user = ask_user_name_and_greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    left_border = 0
    right_border = 100
    while True:
        question = random.randint(left_border, right_border)
        user_ans = ask_question_and_get_answer(question)
        corr_ans = is_parity(question)
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


def is_parity(number):
    return 'yes' if number % 2 == 0 else 'no'
