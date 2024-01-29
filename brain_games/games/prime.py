import prompt
import random
from brain_games import consts


def is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return num == d


def play_prime_number(player_name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(consts.ROUNDS_TO_WIN):

        number = random.randint(*consts.LIMITS_PRIME)

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(f"Question: {number}")
        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(. ",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player_name}!')
