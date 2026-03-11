##SOMA DE TUPLAS

a = (1, 3 ,4)
b =(2, 5, 6, 7, 3)
c = a + b
print(c)
print(len(c))
print(c.count(5)) ##saber quantas vezes tal numero aparece
print(c.index(3)) ##saber em qual posição esta o numero 3

t1 = ('Arthur', 18, 'M', 9.99) ##TUPLAS podem armazenar dados de diferentes tipos
print(t1)

## TUPLAS são imutaveis, mas podem ser apagadas, nao da pra apagar um indice da tupla, somente ela inteira
del(t1)
#print(t1) da erro