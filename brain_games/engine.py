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
    while count < 3:
        question, corr_ans = game_function()
        print('Question: {0}'.format(question))
        user_ans = string('Your answer: ')
        if corr_ans == user_ans and count <= 2:
            print('Correct!')
            count += 1
            continue
        break
    if count == 3:
        print(f'Congratulations, {name_user}!')
    else:
        print(f'"{user_ans}" is wrong answer ;(.', end='')
        print(f'Correct answer was "{corr_ans}".')
        print(f"Let's try again, {name_user}!")
