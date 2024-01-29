import prompt
import random
from brain_games import consts


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return str(num1 + num2)


def play_gcd(player_name):

    print('Find the greatest common divisor of given numbers.')

    for _ in range(consts.ROUNDS_TO_WIN):

        num1 = random.randint(*consts.FIRST_LIMITS_GCD)
        num2 = random.randint(*consts.SECOND_LIMITS_GCD)

        correct_answer = find_gcd(num1, num2)
        print(f'Question: {num1} {num2}')

        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player_name}!')
