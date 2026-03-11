## Definindo funções --- def
def mostraLinha():
    print("---------------------------------------------------------")

mostraLinha()

## Definindo parametros da funcao
def mensagem(msg): ##recebe o parametro
    print('----------------------------')
    print(msg) ##usa o parametro
    print('----------------------------')

mensagem('PARAMETRO ENVIADO')
mensagem(int(input("Digite um numero: ")))

##Conceito de empacotar parametros
def contador( * num): ## *num - diz para o computador que serao recebidos parametros, mas nao se especifica a quantidade, entao ele cria tuplas
    tam = len(num)
    print(f'recebi os valores {num}, e sao ao todo {tam} numeros')
   
    for valor in num:
        print(valor, end=' ')
    print("FIM")


contador(2, 1, 7)
contador(3, 5, 7, 8, 8)

##Para receber listas:

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos +=1


valores = [1,3,4,5,6,2,4,6,3]
print(valores)
dobra(valores)
print(valores)

