lista1 = []
mai = men = 0

indice_maior = 0
indice_menor = 0
for cont in range(0, 5):
    lista1.append(int(input(f"Insira um numero para a posição {cont}: ")))
   
    
    for c, v in enumerate(lista1):
        if cont == 0:
            mai = lista1[0]
            men = lista1[0]
    else:
    
        if lista1[c] > mai:
            mai = lista1[c]
            indice_maior = c
        elif lista1[c] < men:
            men = lista1[c]
            indice_menor = c
    print(lista1)
print(f"O maior número encontrado na lista é {mai}, no índice {indice_maior}")
print(f"O menor numero encontrado na lista é {men}, no indice {indice_menor}")