from random import randint
resposta = randint(0, 10)
got = False
while got == False:
    palpite = int(input("Pensei em um número de 0 a 10, tente adivinhar qual é:\n>>> "))
    if palpite == resposta:
        print("Você venceu, eu pensei no número {}.".format(resposta))
        got = True
    else:
        print("Você errou! Tente novamente...\n")

print("FIM")    