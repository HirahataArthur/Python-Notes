execute = True
maiorn = 0
n1 = 0
n2 = 0
s = 0
while execute:
    print("MENU DA CALCULADORA")
    print("[1] Digite 1 para somar")
    print("[2] Digite 2 para multiplicar")
    print("[3] Digite 3 para saber qual é maior")
    print("[4] Digite 4 para adicionar novos números")
    print("[5] Digite 5 para sair do programa")
    opcao = int(input(">>> "))
    print("\n\n\n")
    
    if opcao == 1:
        s = n1 + n2
        print("Soma entre {} e {} deu: {}.\n\n\n".format(n1, n2, s))
    if opcao == 2:
        s = n1 * n2
        print("O resultado da multiplicação entre {} e {} é {}.\n\n\n".format(n1, n2, s))
    if opcao == 3:
        if n1 > n2:
            maiorn = n1
            print("O maior número é {}.\n\n\n".format(n1))
        if n2 > n1:
            maiorn = n2
            print("O maior número é {}.\n\n\n".format(n2))
        elif n2 == n1:
            print("Os dois números são iguais.\n\n\n")
    if opcao == 4:
        n1 = int(input("Digite o primeiro número\n>>> "))
        n2 = int(input("Digite o segundo número\n>>> "))
    if opcao == 5:
        execute = False
        
