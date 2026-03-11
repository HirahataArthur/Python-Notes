lista1 = []
while True:
    numero = int(input("Digite um valor numerico: "))
    if numero in lista1:
        print("Numero ja presente na lista. Tente novamente...")
    else:
        lista1.append(numero)
        while True:
            opcao = int(input("Quer continuar? [1]SIM [2]NAO\n>>> "))

            if opcao == 1:
                print("Proximo numero...")
                break
            elif opcao == 2:
                print("Encerrando...")
                break  
                
            else:
                print("Resposta nao reconhecida, digite apenas o numero!")
        if opcao == 2:
            break
print(f"Lista com os valores digitados: {lista1}")
lista1.sort()
print(f"Lista em ordem crescente {lista1}")
        
    