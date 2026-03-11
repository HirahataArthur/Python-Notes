maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = int(input("Digite o peso da pessoa:\n>>>"))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    if peso > maiorpeso:
        maiorpeso = peso
        
    if peso < menorpeso:
        menorpeso = peso
print("O maior peso inserido é: {}, e o menor é: {}". format(maiorpeso, menorpeso))
