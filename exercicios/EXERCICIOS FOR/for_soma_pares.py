soma = 0
pares = 0
for c in range(1, 7):
    n = int(input("Digite um número: \n >>>"))
    if n % 2 == 0:
        soma += n
        pares += 1

print("Você informou {} números pares. A soma entre os números pares digitados é: {}".format(pares, soma))