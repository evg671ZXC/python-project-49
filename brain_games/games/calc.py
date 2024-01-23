import prompt
import random


def play_value_expression(player):

    print('What is the result of the expression?')
    for _ in range(3):

        operand_1 = random.randint(1, 100)
        operand_2 = random.randint(1, 50)
        operator = random.choice("+-*")
        if operator == '+':
            value = operand_1 + operand_2
        if operator == '-':
            value = operand_1 - operand_2
        if operator == '*':
            value = operand_1 * operand_2

        correct_answer = f'{value}'

        print(f"Question: {operand_1} {operator} {operand_2}")

        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player}!')
