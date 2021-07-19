#!/usr/bin/env python3
"""This is start progression game."""
from brain_games import engine
from brain_games.games import brain_progression_game


def main():
    """Start progression game."""
    engine.brain_game_logic(brain_progression_game)


if __name__ == '__main__':
    main()
