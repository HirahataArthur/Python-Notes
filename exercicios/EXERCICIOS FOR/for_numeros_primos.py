n1 = int(input("Digite um número: \n>>>"))
tot = 0         ##Contagens de divisões que terminam em 0
for c in range(1, n1 + 1):
    if n1 % c == 0:             
        tot +=1         ##O numero so pode ser dividido ate 2x para ser primo, se passar disto ele não sera considerado primo
if tot == 2:
    print("O numero é primo!")
else:
    print("O numero não é primo!") 
       
