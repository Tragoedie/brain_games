import prompt
from brain_games.scripts.brain_games import main_two


def ask_user_name_and_greeting():
    return main_two()


def ask_question_and_get_answer(data_for_question):
    print('Question: {0}'.format(data_for_question))
    return prompt.string('Your answer: ')


def is_win_or_not(name_user, counter, correct_answer, user_answer):
    right_answer = is_right_answer(name_user, correct_answer, user_answer)
    if right_answer is False:
        return True, counter
    elif counter < 2:
        return False, counter + 1
    print(f'Congratulations, {name_user}!')
    return True, counter


def is_right_answer(name_user, corr_answer, user_answer):
    if corr_answer == user_answer:
        print('Correct!')
        return True
    print(f'"{user_answer}" is wrong answer ;(.', end='')
    print(f'Correct answer was "{corr_answer}".')
    print(f"Let's try again, {name_user}!")
    return False
