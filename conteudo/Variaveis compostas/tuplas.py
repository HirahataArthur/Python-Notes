lanche = ('Suco', 'Hamburguer', 'Refri', 'Pudim')
print(lanche[0]) ##SUCO

print(lanche[2])

print(lanche[0:2]) ##Do indice 0 até o indice 2 (NAO LE O INDICE 2)

print(lanche[-1]) ##de tras pra frente

print(lanche[1:])

print(len(lanche)) ##Numero de elementos dentro de 'lanche'
x = 1
for c in lanche:      ##NAO PRECISA DE POSIÇÃO
   
    print(f"Comida {x}: {c}")
    x +=1   

##  No python NÃO é possivel alterar os elementos dentro das tuplas -- Tuplas são IMUTAVEIS 


#    () TUPLA -------- [] LISTA ------------ {} DICIONÁRIO


for contagem in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[contagem]} na posição  {contagem}")

##Formas similares precisam de posição


for posicao, comida in enumerate(lanche):
    print(f"Vou comer {comida}, posicao {posicao}")

## Comando 'sorted'

print(sorted(lanche))
