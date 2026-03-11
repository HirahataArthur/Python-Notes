num1 = int(input("Digite o primeiro número a ser comparado:"))
num2 = int(input("Digite o segundo número:"))
if num1 == num2:
    print("Os números são iguais")
elif num1 > num2:
    print("O número {} é maior que {}.".format(num1, num2))
elif num1 < num2:
    print("O número {} é menor que {}.".format(num1, num2))