soma = 0
for c in range(0, 501):
    if c % 2 != 0:                       #Para saber se é impar#
        if c % 3 == 0:                   #Para saber se é multiplo de 3#
            soma += c                    #Soma caso antenda as 2 condições#
print("A soma entre todos os multiplos de 3 ímpares entre 0 e 500 é {}".format(soma))
