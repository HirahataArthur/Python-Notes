homemvelho = ''
maioridadehomem = 0
mulher20 = 0
homem = 0
mulher = 0
totalidade = 0
for c in range(1, 5):
    nome = str(input("Digite o nome da pessoa:\n>>> "))
    idade = int(input("Digite a idade dessa pessoa:\n>>> "))
    sexo = int(input("Digite o sexo desta pessoa:\n[1] FEMININO\n[2] MASCULINO\n>>> "))
    if sexo == 2:
        homem += 1
        if idade > maioridadehomem:
            maioridadehomem = idade
            homemvelho = nome
    else:
        mulher += 1
        if idade >= 20:
            mulher20 += 1
    totalidade += idade
media = totalidade/4
print("A média das idades digitas é: {}".format(media))
print("{}, é o homem mais velho com {} anos.".format(homemvelho, maioridadehomem))
print("O número de mulheres acima dos 20 anos é {}".format(mulher20))