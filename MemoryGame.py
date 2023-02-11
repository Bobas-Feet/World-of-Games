import random
import time


def generate_sequence(difficulty):

    try:
        if difficulty == '' or difficulty == ' ':
            print('Error. No blank entries')
        difficulty = int(difficulty)

        rng = []
        for i in range(0, difficulty):
            rng.append(random.randint(1, 101))
        print(rng)

        time.sleep(0.7)
        for b in range(0, 5):
            print('')

        return rng

    except ValueError:
        print('Error')


def get_list_from_user(rng, difficulty):

    for i in range(0, difficulty):
        print('What numbers do you remember seeing? ')
        n = int(input())
        if n == rng[i]:
            print('Correct')
        else:
            print('Wrong. You need to work on you perception more...')
            quit()
            break
    return rng


def is_list_equal(n, rng):
    compare = 'False'
    if set(n) == set(rng):
        compare = 'True'
    return compare


def play(difficulty):
    rng = generate_sequence(difficulty)
    n = get_list_from_user(rng, difficulty)
    is_list_equal(n, rng)
    if is_list_equal(n, rng):
        return 'Yay'
    else:
        return 'Fuck'
