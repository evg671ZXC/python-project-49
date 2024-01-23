#!/usr/bin/env python3
from brain_games import cli
from brain_games.scripts import brain_games
from brain_games.games import calc


def main():

    brain_games.greet()
    calc.play_value_expression(cli.welcome_user())


if __name__ == "__main__":

    main()
