from time import sleep
def contador(inicio, fim, passo):
    
    if fim < inicio:
        if passo < 0:
            passo = +passo
            for c in range(inicio, fim-1, passo):
                print(f'{c} ', end='')
                sleep(0.3)
        else:
            passo = -passo
            for c in range(inicio, fim-1, passo):
                print(f'{c} ', end='')
                sleep(0.3)
    else:
        for c in range(inicio, fim +1, passo):
            print(f'{c} ', end='')
            sleep(0.3)
    
    print("FIM")

print("Contando de 1 até 10 de 1 em 1: ")
contador(1, 10, 1)
print("Contando de 10 até 0 de 2 em 2: ")
contador(10, 0, -2)
print("Agora é a sua vez!")
inicioU = int(input("INICIO: "))
fimU = int(input("FIM: "))
passoU = int(input("PASSO: "))
if passoU < 0:
    passoI = -(passoU)
else:
    passoI = passoU
print(f"Contando de {inicioU} a {fimU} de {passoI} em {passoI}")
contador(inicioU, fimU, passoU)


