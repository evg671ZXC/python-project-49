#!/usr/bin/env python3
import prompt
import random
from brain_games import cli
from brain_games.scripts import brain_games

brain_games.greet()
name = cli.welcome_user()


def find_even():

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct = 0

    while correct < 3:

        count = random.randint(1, 100)
        even_count = count % 2

        print(f"Question: {count}")
        answer = prompt.string('Your answer: ')

        if (even_count == 0 and answer == "yes") or \
           (even_count and answer == "no"):

            print("Correct!")
            correct += 1

        else:
            un_answer = "yes"

            if answer == "yes":
                un_answer = "no"

            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{un_answer}'.")
            break

    if correct == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():

    find_even()


if __name__ == "__main__":

    main()
