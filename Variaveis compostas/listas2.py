##LISTAS DENTRO DE LISTAS
lista1 = list()
lista1.append("Arthur")
lista1.append(18)
print(lista1)
lista2 = list()
lista2.append(lista1[:]) ##COLOCA A LISTA 1 DENTRO DA LISTA 2 - A lista1 inteira é apenas 1 indice dentro da lista 2
print(lista2)

lista3 = []
lista3.append("Maria")
lista3.append(19)
lista2.append(lista3[:]) ##COLOCA A LISTA3 TAMBEM DENTRO DA LISTA 2


print(lista2)
print(lista2[0]) ##INDICE 0 DA LISTA 2 (Lista 1)
print(lista2[1])

print(f"o usuario {lista2[0][0]} tem {lista2[0][1]} anos") ##chamando o conteudo de dentro de uma lista aninhada (dentro da lista2, ache o indice 0, dentro do indice 0, ache o indice 0)

for c in lista2:
    print(f'{c[0]} tem {c[1]} anos de idade.')