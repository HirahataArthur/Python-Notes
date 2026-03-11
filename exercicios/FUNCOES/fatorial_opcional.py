def fatorial(num, show=0):
    f = 1
    if show == 1:
        for c in range(num, 0, -1):
            print(c, end='')
            if c <= 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
                f *= c
        print(f)
        return f
    else:
        for c in range(num, 0, -1):
                f *= c
        
        return f



n1 = int(input("Digite o numero para calcular seu fatorial: "))
opc = str(input("Você gostaria que o processo seja exibido? [s/n]".lower()))
if opc == 's':
   n2 = fatorial(n1, show=1)
else:
   n2 = fatorial(n1, show=0)

print(f'Fatorial de {n1} é {n2}')
