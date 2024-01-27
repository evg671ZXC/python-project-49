import prompt
import random
from brain_games import consts


def play_brain_calc(player_name):

    print('What is the result of the expression?')
    for _ in range(consts.ROUNDS):

        operand_1 = random.randint(consts.MIN_LIMIT, consts.MAX_LIMIT)
        operand_2 = random.randint(consts.MIN_EXTRA_LIMIT, consts.MAX_EXTRA_LIMIT)
        operator = random.choice("+-*")
        if operator == '+':
            value = operand_1 + operand_2
        elif operator == '-':
            value = operand_1 - operand_2
        else:
            value = operand_1 * operand_2

        correct_answer = str(value)

        print(f"Question: {operand_1} {operator} {operand_2}")

        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player_name}!')
