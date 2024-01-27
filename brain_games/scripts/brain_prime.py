#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import prime


def main():

    prime.play_prime_number(cli.welcome_user())


if __name__ == "__main__":

    main()
