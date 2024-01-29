import prompt
import random
from brain_games import consts


def play_brain_calc(player_name):

    print('What is the result of the expression?')
    for _ in range(consts.ROUNDS_TO_WIN):

        num_1 = random.randint(*consts.FIRST_LIMITS_CALC)
        num_2 = random.randint(*consts.SECOND_LIMITS_CALC)
        operator = random.choice("+-*")
        if operator == '+':
            value = num_1 + num_2
        elif operator == '-':
            value = num_1 - num_2
        else:
            value = num_1 * num_2

        correct_answer = str(value)

        print(f"Question: {num_1} {operator} {num_2}")

        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player_name}!')
