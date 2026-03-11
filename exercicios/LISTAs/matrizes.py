matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
for l in range(0, 3): ##linha
    for c in range(0, 3): ##Coluna
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()##sempre que termina uma coluna (3 valores), quebra e vai pra proxima linha
