#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import gcd


def main():

    gcd.play_gcd(cli.welcome_user())


if __name__ == "__main__":

    main()
