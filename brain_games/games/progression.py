import prompt
import random
from brain_games import consts


def get_progression():

    sequence = [random.randint(*consts.START_PROGRESSION)]

    step = random.randint(*consts.STEP_PROGRESSION)

    for i in range(random.randint(*consts.PROGRESSION_LENGTH)):
        sequence.append(sequence[i] + step)

    return sequence


def play_progression_building(player_name):

    print('What number is missing in the progression?')

    for _ in range(consts.ROUNDS_TO_WIN):

        progression = list(map(str, get_progression()))
        index = random.randint(0, len(progression) - 1)

        correct_answer = progression[index]

        progression[index] = ".."

        print(f"Question: {' '.join(progression)}")

        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player_name}!')
