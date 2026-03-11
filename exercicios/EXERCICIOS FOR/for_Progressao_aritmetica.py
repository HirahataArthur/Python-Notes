## ENUNCIADO : Desenvolva um programa que leia o Primeiro termo e a razão de uma PA. No final,
## mostre os 10 primeiros termos dessa progressão

first = int(input("Digite o primeiro termo: \n >>>")) ##Termo de onde começa a progressão
raz = int(input("Digite a razão entre os termos: \n >>>")) ##Diferença entre os termos da progressão
decimo = first + (10 - 1) * raz ##Formula matematica para obter até o décimo termo da PA (Progressão Aritmetica)

for c in range(first, decimo + raz, raz):
    print('{}'.format(c), end=' ')
print("FIM")