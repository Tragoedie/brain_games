"""This is the common games logic."""
from random import randint

from brain_games.scripts.brain_games import main_two


def brain_game_logic(start_str, game_function):
    """Define all game logic.

    Parameters:
        start_str (string): game start string.
        game_function: function for get question and right answer

    Returns: basestring: user name.
    """
    name_user = main_two()
    print(start_str)
    count = 0
    while True:
        question, corr_ans = game_function()
        user_ans = ask_question_and_get_answer(question)
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


def ask_question_and_get_answer(data_for_question):
    """Print question in console and get user answer.

    Parameters:
        data_for_question (string): game question to user.

    Returns:
        basestring: user answer.
    """
    print('Question: {0}'.format(data_for_question))
    return input('Your answer: ')


def is_win_or_not(name_user, counter, correct_answer, user_answer):
    """Check if game is finished.

    Parameters:
        name_user (string): user name.
        correct_answer (string): correct answer, calculated by game.
        user_answer (string): user's answer.
        counter (int): counter of correct given answers.

    Returns:
        bool: is game finished?
    """
    right_answer = is_right_answer(name_user, correct_answer, user_answer)
    if right_answer is False:
        return True, counter
    elif counter < 2:
        return False, counter + 1
    print(f'Congratulations, {name_user}!')
    return True, counter


def is_right_answer(name_user, corr_answer, user_answer):
    """Check if user answer is correct.

    Parameters:
        name_user (string): user name.
        corr_answer (string): correct answer, calculated by game.
        user_answer (string): user's answer.

    Returns:
        bool: is answer correct?
    """
    if corr_answer == user_answer:
        print('Correct!')
        return True
    print(f'"{user_answer}" is wrong answer ;(.', end='')
    print(f'Correct answer was "{corr_answer}".')
    print(f"Let's try again, {name_user}!")
    return False


def get_random_number(left_border=1, right_border=100):
    """Get random number.

    Parameters:
        left_border (int): left border.
        right_border (int): right border.

    Returns:
        integer number: random number
    """
    return randint(left_border, right_border)
