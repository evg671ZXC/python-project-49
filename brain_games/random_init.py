import random


def random_val(limit):

    return random.randint(1, limit)


def random_exp():

    num_1 = random_val(100)
    num_2 = random_val(100)

    operator = random_val(3)

    if operator == 1:
        operator = '+'
    if operator == 2:
        operator = '-'
    if operator == 3:
        operator = '*'

    return f"{num_1} {operator} {num_2}"
