#!/usr/bin/env python3
"""This is start prime game."""
from brain_games.engine import brain_game_logic
from brain_games.games.for_brain_prime import is_prime


def main():
    """Start prime game."""
    start_str = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_game_logic(start_str, is_prime)


if __name__ == '__main__':
    main()
