s = 0
while True:
    n1 = int(input("Digite o numero do qual deseja obter a tabuada:\n>>> "))
    if n1 < 0:
        print("Finalizando...")
        break
    n2 = int(input("Digite ate que valor deseja multiplicar o anterior\n>>> "))
    
    for c in range(1, n2+1):
        s = n1 * c
        print(f"{n1} x {c} = {s}")
print("FIM")