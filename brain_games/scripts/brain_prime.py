import prompt
from brain_games import cli
from brain_games import random_init
from brain_games.scripts import brain_games

brain_games.greet()
name = cli.welcome_user()


def check_is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return num == d


def find_prime_num():

    print('What is the result of the expression?')

    correct = 0

    while correct < 3:
        number = random_init.random_val(100)

        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')

        if answer == 'yes' and check_is_prime(number):
            print('Correct!')
            correct += 1
        elif answer == 'no' and not check_is_prime(number):
            print('Correct!')
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

    find_prime_num()


if __name__ == "__main__":

    main()
