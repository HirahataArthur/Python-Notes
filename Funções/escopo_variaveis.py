##variaveis que so funcionam em tais areas
## exemplo:

def teste():
    x = 8 ## "x" é uma variavel LOCAL, so funciona dentro da sua função
    print(f'dentro da função "n" vale {n}')
    print(f'Dentro da função "x" vale {x}')

n = 2 ## "n" é uma variavel global, funciona no programa todo
teste()
print(f'Fora da função "n" vale {n} ')
print('Fora da função x não vale nada, pois foi declarada localmente, se tentar chama-la da erro:')
##print(x)
print('~'*30)

## Porem, é possivel definir que a função utilize a variavel global ao inves de usar a propria:
a = 2
print(f'Valor de a {a}')
def teste2():
    global a ##ordem pra que ele use a variavel global
    a +=  8
    print(f'Valor de a dentro da função: {a}')
teste2()
print(f"Valor de a fora da função segue sendo {a}, pois foi alterada a variavel global, e nao uma copia da mesma")


##RETORNANDO VALORES
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s ##Ao inves de retornar uma impressao como anteriormente, definimos que ele retorne s como resposta a chamada da função

r1 = soma(3, 5, 6) ##Oque significa que r1 valera o retorno da função, que é a soma de seus parametros nesse exemplo
r2= soma(4,6)
r3= soma(2)

print(f"Os resultados foram {r1}, {r2} e {r3}")