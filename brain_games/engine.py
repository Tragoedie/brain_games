"""This is the common games logic."""
import prompt

CORRECT_ANSWERS_TO_WIN = 3


def brain_game_logic(game_pack):
    """Define all game logic.

    Parameters:
        game_pack: this is game logic package

    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game_pack.get_start_game_string())
    right_answer_counter = 0
    while right_answer_counter < CORRECT_ANSWERS_TO_WIN:
        question, correct_answer = game_pack.get_question_and_correct_answer()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            break
        print('Correct!')
        right_answer_counter += 1
    if right_answer_counter == CORRECT_ANSWERS_TO_WIN:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print(
            '"{0}" is wrong answer ;(. Correct answer was "{1}".'.
            format(user_answer, correct_answer),
        )
        print("Let\'s try again, {0}!".format(user_name))
