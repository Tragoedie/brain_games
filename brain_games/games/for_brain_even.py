"""This is the even game logic."""

from brain_games.games.engine import brain_game_logic, get_random_number


def brain_even_logic():
    """Define even game logic."""
    start_str = 'Answer "yes" if given number is even. Otherwise answer "no".'
    brain_game_logic(start_str, is_parity)


def is_parity():
    """Check if number is odd.

    Returns:
        basestring: returns expression with result.
    """
    number = get_random_number()
    return number, 'yes' if number % 2 == 0 else 'no'
