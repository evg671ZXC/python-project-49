import prompt
from brain_games import cli
from brain_games import random_init
from brain_games.scripts import brain_games

brain_games.greet()
name = cli.welcome_user()


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def play_gcd():

    print('Find the greatest common divisor of given numbers.')

    correct = 0

    while correct < 3:
        num_1 = random_init.random_val(100)
        num_2 = random_init.random_val(100)

        print(f'Question: {num_1} {num_2}')
        gcd = find_gcd(num_1, num_2)

        answer = prompt.string('Your answer: ')
        if answer == str(gcd):
            print('Correct!')
            correct += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{str(gcd)}'.")
            break

    if correct == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():

    play_gcd()


if __name__ == "__main__":

    main()
