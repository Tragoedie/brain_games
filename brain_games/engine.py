"""This is the common games logic."""
from prompt import string


def brain_game_logic(start_str, game_function):
    """Define all game logic.

    Parameters:
        start_str (string): game start string.
        game_function: function for get question and right answer

    Returns: basestring: user name.
    """
    print('Welcome to the Brain Games!')
    name_user = string('May I have your name? ')
    print('Hello, {0}!'.format(name_user))
    print(start_str)
    count = 0
    while True:
        question, corr_ans = game_function()
        print('Question: {0}'.format(question))
        user_ans = string('Your answer: ')
        win_or_lose, count = is_win_or_not(name_user, count, corr_ans, user_ans)
        if win_or_lose:
            break


def is_win_or_not(name_user, counter, correct_answer, user_answer):
    """Check if game is finished.

    Parameters:
        name_user (string): user name.
        correct_answer (string): correct answer, calculated by game.
        user_answer (string): user's answer.
        counter (int): counter of correct given answers.

    Returns:
        bool: is game finished? and counter
    """
    if correct_answer == user_answer and counter < 2:
        print('Correct!')
        return False, counter + 1
    elif correct_answer == user_answer and counter == 2:
        print(f'Congratulations, {name_user}!')
    else:
        print(f'"{user_answer}" is wrong answer ;(.', end='')
        print(f'Correct answer was "{correct_answer}".')
        print(f"Let's try again, {name_user}!")
    return True, counter
