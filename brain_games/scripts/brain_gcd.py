#!/usr/bin/env python3
"""This is start NOD game."""
from brain_games import engine
from brain_games.games import brain_gcd_game


def main():
    """Start Even game."""
    engine.brain_game_logic(brain_gcd_game)


if __name__ == '__main__':
    main()
