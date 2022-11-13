import itertools
import random
import string

#Reference: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
def KeyGeneration(length):
    #It generates a random key of uppercase letters of a given length
    alphabet = string.ascii_uppercase
    return ''.join(random.choice(alphabet) for _ in range(length))


def KeyCombinations(length):
    #It takes a length and returns all possible key combinations of that length
    alphabet = string.ascii_uppercase
    yield from itertools.product(alphabet, repeat=length)


if __name__ == '__main__':
    for _ in range(5):
        print(KeyGeneration(10))

    with open('KeysAllow.txt', 'w') as f:
        for key in KeyCombinations(3):
            f.write(f'{key}\n')