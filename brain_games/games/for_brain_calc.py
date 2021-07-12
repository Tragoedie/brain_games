"""This is the calculator game logic."""
import random

from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    get_random_number,
    is_win_or_not,
)


def brain_calc_logic():
    """Define calculator game logic."""
    name_user = ask_user_name_and_greeting()
    print('What is the result of the expression?.')
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
    operator = random.choice('+-*')
    if operator == '+':
        expression_result = number_one + number_two
    elif operator == '-':
        expression_result = number_one - number_two
    else:
        expression_result = number_one * number_two
    return f'{number_one}{operator}{number_two}', str(expression_result)
