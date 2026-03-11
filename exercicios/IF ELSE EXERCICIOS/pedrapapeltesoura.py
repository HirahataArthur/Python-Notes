opcao = int(input('''VAMOS JOGAR UM JOGO DE PEDRA PAPEL OU TESOURA:\n SELECIONE SUA OPÇÃO:
[1] PEDRA
[2] PAPEL
[3] TESOURA \n>>> '''))

if opcao == 1:
    player = "PEDRA"
elif opcao == 2:
    player = "PAPEL"
elif opcao == 3:
    player = "TESOURA"


from random import randint
computador = randint(1, 3)


if computador == 1:
    pcchoice = "PEDRA"
elif computador == 2:
    pcchoice = "PAPEL"
elif computador == 3:
    pcchoice = "TESOURA"
print("Eu escolhi {}.".format(pcchoice))
print("Você escolheu {}.".format(player))

if player == pcchoice:
    print("Houve um empate! Escolhemos a mesma opção!")
elif player == "PAPEL":
    if pcchoice == "PEDRA":
        print("Você venceu!")
    else:
        print("Eu venci!")
elif player == "PEDRA":
    if pcchoice == "TESOURA":
        print("Você venceu!")
    else:
        print("Eu venci!")
elif player == "TESOURA":
    if pcchoice == "PAPEL":
        print("Você venceu!")
    else:
        print("Eu venci!")
