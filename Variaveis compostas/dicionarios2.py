estado = dict()
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input("Digite o nome do estado: "))
    estado['Sigla'] = str(input("Digite a sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")