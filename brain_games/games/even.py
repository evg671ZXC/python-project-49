import prompt
import random
from brain_games import consts


def play_even_value(player_name):

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(consts.ROUNDS):

        value = random.randint(consts.MIN_LIMIT, consts.MAX_LIMIT)

        print(f"Question: {value}")
        player_answer = prompt.string('Your answer: ')

        if value % 2:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player_name}!')
