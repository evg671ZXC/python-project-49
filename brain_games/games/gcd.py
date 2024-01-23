import prompt
import random


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return f"{num1 + num2}"


def play_gcd(player):

    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):

        one = random.randint(1, 100)
        two = random.randint(1, 100)

        gcd = find_gcd(one, two)
        print(f'Question: {one} {two}')

        player_answer = prompt.string('Your answer: ')

        if player_answer != gcd:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{gcd}'.\n",
                  f"Let's try again, {player}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {player}!')
