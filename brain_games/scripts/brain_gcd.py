#!/usr/bin/env python3
"""This is start NOD game."""
from brain_games.engine import brain_game_logic
from brain_games.games.for_brain_gcd import generate_nod_numbers


def main():
    """Start Even game."""
    start_str = 'Find the greatest common divisor of given numbers.'
    brain_game_logic(start_str, generate_nod_numbers)


if __name__ == '__main__':
    main()
