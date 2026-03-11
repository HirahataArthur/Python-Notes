
##com função importada da tecnologia

from math import factorial
n = int(input("Digite um número para calcular seu fatorial"))
f = factorial(n)
print("O fatorial de {}, é {}.".format(n, f))



##COm while

n = int(input("Digite um numero pra calcular fatorial:\n>>> "))
c = n
f = 1

print("Calculando {}! = ".format(n), end='')
while c > 0:
    print("{}".format(c), end='')
    if c > 1:
        print(" x ", end='')
    else:
        print(" = ", end='')
    f = f*c
    c -= 1
print("{}".format(f), end='')


##tentar com o for agr:

n2 = int(input("Digite um numero para calcular fatorial:\n>>> "))
c2 = n2
f2 = 1

print("Calculando {}! >>> ".format(c2), end='')
for c2 in range(c2, 0, -1):
    print("{}".format(c2), end='')
    if c2 <= 1:
        print(" = ", end='')
    else:
        print(" x ", end='')
    f2 *= c2
print("{}".format(f2))