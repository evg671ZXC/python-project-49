import prompt
from brain_games import cli
from brain_games import random_init
from brain_games.scripts import brain_games

brain_games.greet()
name = cli.welcome_user()


def find_value_progres():

    print('What number is missing in the progression?')
    question = ".."

    correct = 0

    while correct < 3:

        progres = random_init.correct_prog()
        index = random_init.get_random_choice(progres)

        win_answer = progres[index]

        hidden_prog = [] + progres
        hidden_prog[index] = question
        str_hidden_prog = ' '.join(hidden_prog)
        print(f"Question: {str_hidden_prog}")

        user_answer = prompt.string('Your answer: ')

        if user_answer == str(win_answer):
            print('Correct!')
            correct += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ",
                  f"Correct answer was '{str(win_answer)}'.")
            break

    if correct == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():

    find_value_progres()


if __name__ == "__main__":

    main()
