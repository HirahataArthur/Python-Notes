cont = 0
s = 0
while True:
    numero = int(input("Digite um numero para adicionar a soma:\n>>> "))
    if numero == 999:
        print("Finalizando...")
        break
    s = numero + s
    cont += 1
    print("Digite 999 para somar")
print(f"a soma dos {cont} valores inseridos é {s}")