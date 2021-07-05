"""Ask user name, and greeting user."""
import prompt


def welcome_user():
    """Ask user name, and greeting user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
