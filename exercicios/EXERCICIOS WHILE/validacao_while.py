requisito =  0
while requisito != 1:
    sexo = str(input("Qual é o seu sexo?\n [F] Feminino  ou [M] Masculino\n>>> "))
    if sexo == 'F':
        print("Certo, você é femea kk")
        requisito += 1
    if sexo == 'M':
        requisito += 1
        print("Certo, você é macho kk")
    if sexo != 'F':
        if sexo != 'M':
         print("ERRO, Digite a opção de acordo com a formatação")
print("FIM")