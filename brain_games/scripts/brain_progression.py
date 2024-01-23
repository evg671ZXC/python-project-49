#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import progression
from brain_games.scripts import brain_games


def main():

    brain_games.greet()
    progression.play_progression_building(cli.welcome_user())


if __name__ == "__main__":

    main()
