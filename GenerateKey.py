import itertools
import random
import string


def KeyGneration(length):
    #It generates a random key of uppercase letters of a given length
    alphabet = string.ascii_uppercase
    return ''.join(random.choice(alphabet) for _ in range(length))


def KeyCombinations(length):
    #It takes a length and returns all possible key combinations of that length
    alphabet = string.ascii_uppercase
    yield from itertools.product(alphabet, repeat=length)


if __name__ == '__main__':
    for _ in range(10):
        print(KeyGneration(5))

    with open('KeysAllow.txt', 'w') as f:
        for key in KeyCombinations(4):
            f.write(f'{key}\n')