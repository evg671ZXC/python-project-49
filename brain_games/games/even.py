import prompt
import random


def play_even_value(player):

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):

        value = random.randint(1, 100)

        print(f"Question: {value}")
        player_answer = prompt.string('Your answer: ')

        if value % 2:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player}!')
