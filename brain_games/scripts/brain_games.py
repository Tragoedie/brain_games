#!/usr/bin/env python3
"""This is start game."""
from brain_games.cli import welcome_user


def main_two():
    """Print initial load screen.

    Returns:
        basestring: user name.
    """
    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main = main_two()
