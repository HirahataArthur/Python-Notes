numeros = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    escolha = int(input("Digite um numero entre 1 e 20\n"))
    if escolha > 20:
        print("Tente novamente\n")
    elif escolha < 1:
        print("Tente novamente\n")
    else:
        break
print(f"Então você digitou o número {numeros[escolha - 1]}")
        
