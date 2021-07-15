#!/usr/bin/env python3
"""This is start calculator game."""
from brain_games.engine import brain_game_logic
from brain_games.games.for_brain_calc import generate_expression


def main():
    """Start Calculator game."""
    start_str = 'What is the result of the expression?.'
    brain_game_logic(start_str, generate_expression)


if __name__ == '__main__':
    main()
