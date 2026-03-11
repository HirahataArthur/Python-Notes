def leiaInt(msg):
    while True:
        try: 
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: Formato incorreto, por favor digite um numero inteiro valido!")
            continue
        else:
            return n1  
def leiaFloat(msg):
    while True:
        try: 
            n1 = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO: Formato incorreto, por favor digite um numero inteiro valido!")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuario.")
            return 0

        else:
            return n1
        


num = leiaInt("Digite um numero inteiro: ")
num2 = leiaFloat("Digite um numero real:")
print(f"Você digitou o numero: {num}")
print(f"Voce digitou o numero real: {num2}")

