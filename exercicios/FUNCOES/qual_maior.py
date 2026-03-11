from time import sleep
def maior(lst):
    print("Analisando numeros recebidos...")
    maior = lst[0]
    for c in lst:
        print(f"{c} ", end='')
        sleep(0.4)
        if c > maior:
            maior = c

    print(f"Foram informados {len(lst)} valores ao todo.")
    sleep(0.4)
    print(f"O maior numero dentre os recebidos é: {maior}")

numeros = []
while True:
    numeros.append(int(input("Digite um numero: ")))
    op = str(input("Quer continuar? [s/n] ").lower())
    if op == 'n':
        break
maior(numeros)