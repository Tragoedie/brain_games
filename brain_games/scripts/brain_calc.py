#!/usr/bin/env python3
"""This is start calculator game."""
from brain_games import engine
from brain_games.games import brain_calc_game


def main():
    """Start Calculator game."""
    engine.brain_game_logic(brain_calc_game)


if __name__ == '__main__':
    main()
