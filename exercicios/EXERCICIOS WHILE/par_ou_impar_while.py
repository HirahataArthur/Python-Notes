from random import randint
from time import sleep

s = 0
vitorias = 0
while True:
    computador = randint(0, 100)
    guess = str(input("PAR OU IMPAR?\n [P] ou [I]\n>>> "))
    if guess == 'P': 
        numeroPlayer = int(input("Digite o seu numero\n>>> "))
    elif guess == 'I':
        numeroPlayer = int(input("Digite o seu numero\n>>> "))
    else:
        print("Entrada não reconhecida")
        break
    s = numeroPlayer + computador
    print(f"Eu pensei no número {computador}, você pensou no número {numeroPlayer}. A soma dos nossos números é {s}")

    if s % 2 == 0:
        if guess == 'P':
            print("Como você escolheu PAR você ganhou! Vamos denovo!")
            print("+1 vitória")
            vitorias += 1
            sleep(1)
            print("Carregando...")
            sleep(2)
        else:
            sleep(3)
            print("Já que você escolheu ÍMPAR, você perdeu!")
           
            print(f"Total de vitórias {vitorias}")
            break
    else:
        if guess == 'I':
            print(" Como você escolheu ÍMPAR, você ganhou! Vamos denovo!")
            print("+1 vitória")
            vitorias += 1
            sleep(1)
            print("Carregando...")
            sleep(2)
        else:
            sleep(3)
            print("Já que você escolheu PAR, você perdeu!")
           
            print(f"Total de vitórias {vitorias}")
            break
print("FIM")






