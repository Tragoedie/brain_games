#!/usr/bin/env python3
"""This is start Even game."""
from brain_games.engine import brain_game_logic
from brain_games.games.for_brain_even import is_parity


def main():
    """Start Even game."""
    start_str = 'Answer "yes" if given number is even. Otherwise answer "no".'
    brain_game_logic(start_str, is_parity)


if __name__ == '__main__':
    main()
