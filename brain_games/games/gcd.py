import prompt
import random


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def play_gcd(name):

    print('Find the greatest common divisor of given numbers.')

    correct = 0

    while correct < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)

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
