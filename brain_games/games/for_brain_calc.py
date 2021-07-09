import random

from brain_games.games.engine import (
    ask_question_and_get_answer,
    ask_user_name_and_greeting,
    is_win_or_not,
)


def brain_calc_logic():
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
    left_border = 0
    right_border = 100
    number_one = random.randint(left_border, right_border)
    number_two = random.randint(left_border, right_border)
    operator = random.choice('+-*')
    if operator == '+':
        expression_result = number_one + number_two
    elif operator == '-':
        expression_result = number_one - number_two
    else:
        expression_result = number_one * number_two
    return f'{number_one}{operator}{number_two}', str(expression_result)
