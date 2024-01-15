import prompt
import random


def check_is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return num == d


def find_prime_num(name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct = 0

    while correct < 3:
        number = random.randint(1, 100)

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
