# Python
import os
import sys

import rc4 as rc4
from GenerateKey import KeyGeneration, KeyCombinations
from stats import cpuStats

# PRINT COLORS
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
PINK = '\033[95m'
RED = '\033[31m'
BLUE = '\033[34m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
PURPLE = '\033[35m'

"""
Toma un archivo dato, se genera una clave de un determinado tamaño y
luego se encripta con el algoritmo rc4. Además genera un archivo de respaldo
que posteriormente sirve para comprobar si se desencripta correctamente
@param filename: el nombre del archivo a encriptar
@param keyLen: El tamaño de la llave que se va a usar
"""
def encrypt(filename, keyLen):
    with open(filename, 'r') as f:
        content = f.read()

    with open(nameAux(filename), 'w') as f:
        f.write(content)

    keyGenerated = KeyGeneration(keyLen)
    print(OKGREEN + '+'*50 + ENDC)
    print(f'Tamaño de la llave: {keyLen}')
    print(f'Llave usada para encriptar: {keyGenerated}\n')
    encryptedContent = rc4.encrypt(content, keyGenerated)

    with open(filename, 'w') as f:
        f.write(str(encryptedContent))

"""
Toma el archivo encriptado, se generan todas las posibles llaves para probar
desencriptarlo hasta que el resultado sea igual que el archivo original, en este
caso el de respaldo
@param filename: nombre del archivo a desencriptar
@param keyLen: El tamaño de la llave que se va a usar
"""
@cpuStats
def decryptBruteForce(filename, keyLen):
    with open(filename, 'r') as f:
        encryptedContent = f.read()

    with open(nameAux(filename), 'r') as f:
        originalContent = f.read()

    counter = 0
    for key in KeyCombinations(keyLen):
        counter += 1
        sys.stdout.write('\033[F')
        print(f'Llave probada: {"".join(key)} -> [{counter}/{26**keyLen}]') #26 es por las letras del abecedario inglés
        decryptedContent = rc4.decrypt(encryptedContent, key)
        if originalContent == str(decryptedContent):
            with open(filename, 'w') as f:
                f.write(str(decryptedContent))
            print(f'Desencriptado con la llave: {"".join(key)}')
            break
    print(OKGREEN + '+'*50 + ENDC)


"""
Toma el nombre original y le agrega un -bk 
@param filename: el nombre del archivo a generarle el nombre con el bk
@return: el nombre del archivo con el -bk agregado
"""
def nameAux(filename):
    f = filename.split('.')
    f.insert(len(f)-1, '-bk.')
    return ''.join(f)

if __name__ == '__main__':

    filename = str(sys.argv[1]) # first argument
    keyLen = int(sys.argv[2]) # second argument

    encrypt(filename, keyLen)
    decryptBruteForce(filename, keyLen)

    os.remove(nameAux(filename)) #se elimina el archivo de respaldo
