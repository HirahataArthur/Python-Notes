from random import randint
from time import sleep
numeros = list()


def sorteia():
    print("Sorteando 5 valores...")
    for c in range(0, 5):
        n = randint(0, 100)
        print(f'{n} ', end='')
        numeros.append(n)
        sleep(0.4)
    print("PRONTO")
    print('---------------------------------')

def somando(lst):
    soma = 0

    for c in lst:
        if c%2 == 0:
            soma += c
    print(f"A soma dos valores pares de {lst} é: {soma}")


sorteia()
sleep(1)
somando(numeros)
