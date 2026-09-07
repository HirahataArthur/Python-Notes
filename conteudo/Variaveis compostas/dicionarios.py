## Dicionarios sao estruturas de dados semelhantes a tuplas e listas, porem seus indices podem ter nomes literais
## Dicionarios sao declarados utilizando chaves {}
dados = dict() ## ou 
dados = {'nome': 'Arthur', 'idade':18} ##Cria-se o indice nome, que comporta 'Arthur', e o indice idade, comportando 18
print(dados['nome'])

##outra forma de criar indice:
dados['sexo'] = 'M' ##Indice sexo, comportando 'M'
print(dados['sexo'])
print(dados)

##para remover elementos:
del dados['sexo']
print(dados)

##Para imprimir apenas os valores de cada chave
print(dados.values())

##Para imprimir apenas as chaves:
print(dados.keys())

#Para imprimir os 2:
print(dados.items())


##Exemplo pratico com for
filmes = {"titulo": "Star Wars", "ano":1970, "Diretor":"George Luccas"}
for k, v in filmes.items():
    print(f"O {k} é {v}")

##É possivel colocar dicionarios dentro de listas e vice versa
## Exemplo
locadora = []
locadora.append(filmes)
print(locadora[0]['ano'])

## Entre listas e dicionarios nao da pra usar [:] para copiar, precisa-se usar .copy()