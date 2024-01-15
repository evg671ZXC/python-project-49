import random


def random_exp():

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)

    operator = random.randint(1, 3)

    if operator == 1:
        operator = '+'
    if operator == 2:
        operator = '-'
    if operator == 3:
        operator = '*'

    return f"{num_1} {operator} {num_2}"


def random_prog():

    sequence = []

    start = random.randint(1, 30)
    end = random.randint(31, 50)
    step = random.randint(1, 5)

    for i in range(start, end, step):
        sequence.append(str(i))

    return sequence


def correct_prog():

    correct = random_prog()

    while len(correct) < 10:
        correct = random_prog()

    return correct[0:random.randint(5, 10)]


def get_random_choice(my_prog):

    random_index = random.randint(0, len(my_prog) - 1)

    return random_index
