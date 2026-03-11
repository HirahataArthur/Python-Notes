from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    birth = int(input("Digite o ano em que esta pessoa nasceu: \n>>>"))
    age = atual - birth
    if age >= 18:
        print("Esta pessoa é maior de idade.")
        maior += 1
    else:
        print("Esta pessoa é menor de idade.")
        menor += 1
print("O número de pessoas que atingiram a maioridade é: {}, enquanto o número de pessoas que não atingiram é: {}".format(maior, menor))
    