emprestimocasa = int(input("Qual o valor do imóvel a ser adquirido?\nR$"))
salario = int(input("Digite seu salário: \nR$"))
tempo = int(input("Por último digite em quantos anos pretende pagar o imóvel: \n"))
prestacaoMensal = (emprestimocasa/tempo)/12
limite = salario*(30/100)
if prestacaoMensal > limite:
    print("Empréstimo Negado! O Valor das prestações mensais {} ultrapassa 30%. da renda de R${}!".format(prestacaoMensal, salario))
else:
    print("Empréstimo Aprovado! \n RECAPTULAÇÃO:")
    print("Imóvel no valor de R${}, será pago em prestações mensais de R${} durante {} anos.".format(emprestimocasa, prestacaoMensal, tempo))
    print("Sem exceder o limite de 30% (R${}) nas prestações mensais, referente ao salário: R${}".format(limite, salario))