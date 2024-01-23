import prompt
import random


def get_progression():

    sequence = [random.randint(1, 30)]

    step = random.randint(1, 5)

    for i in range(10):
        sequence.append(sequence[i] + step)

    return sequence[:random.randint(5, 10)]


def get_random_index(sequence):

    index = random.randint(0, len(sequence) - 1)

    return index


def play_progression_building(player):

    print('What number is missing in the progression?')

    for _ in range(3):

        progression = list(map(str, get_progression()))
        index = get_random_index(get_progression())

        correct_answer = progression[index]

        output_progression = progression.copy()
        output_progression[index] = ".."

        print(f"Question: {' '.join(output_progression)}")

        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.\n",
                  f"Let's try again, {player}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player}!')
