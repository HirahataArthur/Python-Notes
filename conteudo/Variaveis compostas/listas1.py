##LISTAS - LISTAS SÃO MUTAVEIS - PODEM SER MODIFICADAS 

lista1 = ['Arthur', 'Maria', 'Alexandre', 'Solange', 'Davi']
print(lista1[1])
print(f"{lista1}")

lista1[1] = 'Maria Luisa' ##modificando a lista
print(lista1[1])
print(f"{lista1}")

##ADICIONAR ELEMENTOS A LISTA
lista1.append('Naomi') ##Adiciona no final
print(lista1[5])
print(f"{lista1}")

lista1.insert(0, 'Nomes:') ##insere novo elemento no indice 0, e empurra todos os outros 1 indice pra frente
print(lista1[2])
print(f"{lista1}")

##APAGAR ELEMENTOS
del lista1[0] ##deleta pelo indice
print(f"{lista1}")
lista1.pop(5) ##geralmente usado para deletar o ultimo, mas pode ser usado para deletar pelo indice tbm
print(f"{lista1}")
lista1.remove('Davi') ##Deleta pelo conteudo
print(f"{lista1}")

##LISTAS ATRAVES DE RANGES
valores = list(range(4,11))
print(f"{valores}")
