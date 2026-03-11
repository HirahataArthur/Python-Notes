from random import randint
computador = randint(0, 5)

palpite = int(input("Tente adivinhar o número em que estou pensando:"))
if palpite == computador:
    print("EXATAMENTE")
else:
    print("INCORRETO")