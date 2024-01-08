import prompt
from brain_games import cli
from brain_games import random_init
from brain_games.scripts import brain_games

brain_games.greet()
name = cli.welcome_user()


def find_value():

    print('What is the result of the expression?')

    correct = 0

    while correct < 3:
        expression = random_init.random_exp()
        value = eval(expression)
        print('Question: ' + expression)
        answer = prompt.string('Your answer: ')
        if answer == str(value):
            print('Correct!')
            correct += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{str(value)}'.")
            break

    if correct == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():

    find_value()


if __name__ == "__main__":

    main()
