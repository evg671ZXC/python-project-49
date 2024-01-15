import prompt
from brain_games import random_init


def find_value(name):

    print('What is the result of the expression?')

    correct = 0

    while correct < 3:
        expression = random_init.random_exp()
        value = eval(expression)
        print('Question: ' + expression)
        answer = prompt.string('Your answer: ')
        if answer == str(value):
            print('Correct!')
            correct += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{str(value)}'.")
            break

    if correct == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
