"""This is the prime game logic."""

from brain_games.games.engine import brain_game_logic, get_random_number


def brain_prime_logic():
    """Define prime game logic."""
    start_str = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_game_logic(start_str, is_prime)


def is_prime():
    """Check if number is prime.

    Returns:
        basestring: returns expression with result.
    """
    number = get_random_number()
    if number % 2 == 0:
        return number, 'no'
    step = 3
    while step * step <= number and number % step != 0:
        step += 2
    return number, 'yes' if step * step > number else 'no'
