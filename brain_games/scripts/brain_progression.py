#!/usr/bin/env python3
"""This is start progression game."""
from brain_games.engine import brain_game_logic
from brain_games.games.for_brain_progression import generate_progression


def main():
    """Start progression game."""
    start_str = 'What number is missing in the progression?.'
    brain_game_logic(start_str, generate_progression)


if __name__ == '__main__':
    main()
