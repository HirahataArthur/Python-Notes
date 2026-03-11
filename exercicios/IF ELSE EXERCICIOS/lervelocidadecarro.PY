velocidade = int(input("Qual é a velocidade do carro em km/h? \n"))
if velocidade > 80:
    multa = 7*(velocidade - 80)
    print("Limite excedido! Você foi multado em R${}!".format(multa))
else:
    print("Limite respeitado! Tenha um bom dia!")