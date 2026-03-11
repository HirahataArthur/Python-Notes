## Erros e Excessões
## Quando o erro nao esta na sintaxe, é dado o nome de 'excessão'
## Para tratar, utilizar estrutura 'try' 'except' 'else' 'finally' (else e finally sao opcionais)
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite ouotro numero: "))
    s = n1 / n2
except Exception as erro: ##se der problema executa esse
    print(f"Ocorreu um problema: {erro.__class__}")
else: ##se nao der problema
        print(f"A divisao de {n1} por {n2} é: {s}.")
finally: ##Acontece independente da falha existir ou nao
     print("FIM") 

##Para mostrar o erro: 
try:
    a =1
    b = 0
    s = a/b
except Exception as erro: ##mostra o erro
     print(f"Problema encontrado foi:{erro.__class__}") ##imprimindo o erro


##Pode-se ter varios tipos de exception, cada um com seu bloco de tratamento:
try:
     n1 = int(input("Numero 1: "))
     n2 = int(input("numero 2: "))
     s = n1/n2
except (TypeError, ValueError):##Tratamento especifico para este erro(exceção)
     print("Ocorreu um erro com o tipo de dado digitado")
except ZeroDivisionError: ##Tratamento especifico para este erro(exceção)
     print("Nao é possivel dividir por 0")     
else:
     print(f"{n1} / {n2} = {s}")
finally:
     print("FIM")