temporaria = []
principal = []
mai = men = 0
while True:
    temporaria.append(str(input("Nome: ")))
    temporaria.append(float(input("Peso: ")))
    
    if len(principal) == 0:
        mai = men = temporaria[1]
        print("Primeiro peso")
    else:
        if temporaria[1] > mai:
            mai = temporaria[1]
        elif temporaria[1] < men:
            men = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input("Quer continuar? [s/n]"))
    if resp in 'Nn':
        break

print(f"Ao todo foram cadastradas {len(principal)} pessoas.")
print(f"O maior peso encontrado foi: {mai}kg peso de: ", end='')
for p in principal:
    if p[1] == mai:
        print(f"[{p[0]}]")
print(f"O menor peso encontrado foi {men}kg. Peso de: ", end='')
for p in principal:
    if p[1] == men:
        print(f"{p[0]}")
