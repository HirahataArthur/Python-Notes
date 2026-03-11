matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
soma = 0
soma3 = 0
maior2 = 0
for l in range(0, 3): ##linha
    for c in range(0, 3): ##Coluna
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0: ## Para somar numeros pares 
            soma += matriz[l][c]
        if c == 2: ## Somar os valores da terceira coluna
            soma3 += matriz[l][c]
        if l == 1:  ## Analisar os numeros da segunda linha, instituindo o primeiro como o maior, e comparando ele com o resto
            if c == 0: ##Primeiro numero da linha 2 (coluna 0) é por padrao o maior
                maior2 = matriz[l][c]
            else:
                if matriz[l][c] > maior2:
                    maior2 = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()##sempre que termina uma coluna (3 valores), quebra e vai pra proxima linha
print(f"A soma de todos os numeros pares digitados é: {soma}")
print(f"A soma dos valores da terceira coluna são: {soma3}")
print(f"O maior numero da segunda linha é : {maior2}")

