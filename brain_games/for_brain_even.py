import random

import prompt
from brain_games.scripts.brain_games import main_two


def brain_even_logic():
    name_user = main_two()
    counter_right_answer = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter_right_answer < 3:
        right_answer = game(name_user)
        if right_answer:
            counter_right_answer += 1
        else:
            return
    print('Congratulations, {0}!'.format(name_user))


def game(name_user):
    random_number = random.randint(0, 100)
    user_answer = prompt.string('Question: {0}\n'.format(random_number))
    is_parity = parity_check(random_number)
    if is_parity and user_answer == 'yes':
        print('Correct!')
        return True
    elif not is_parity and user_answer == 'no':
        print('Correct!')
        return True
    return end_game(name_user, is_parity, user_answer)


def end_game(name_user, is_parity, user_answer):
    if is_parity and user_answer == 'no':
        print("'no' is wrong answer;(. Correct answer was 'yes'.")
    elif not is_parity and user_answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    print("Let's try again, {0}!".format(name_user))
    return False


def parity_check(number):
    return number % 2 == 0

