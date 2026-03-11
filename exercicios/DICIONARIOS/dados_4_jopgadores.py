from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), ## Dicionario inicial, com o jogador e o numero sorteado
        'jogador2': randint(1, 6),
        'joagdor3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list() ##Dicionario novo de ranking
print('Valores sorteados')
for k, v in jogo.items():
    print(f'O {k} sorteou o valor {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-*' *30)
for i, v in enumerate(ranking):
    print(f"O {i + 1} lugar: {v[0]} com {v[1]}.")

