
from pathlib import Path


PASTA_DO_EXERCICIO = Path(__file__).resolve().parent


with open(PASTA_DO_EXERCICIO / "frases.txt", 'r', encoding='utf-8') as arquivo: ##MÉTODO COUNT, PARA REALIZAR CONTAGENS DE ELEMENTOS
    ler = arquivo.read()
    contar = ler.count('l')
    print(f"Contagem de 'l' =  {contar}") ##CONTAGEM SUPERFICIAL, CONTA TODOS OS ELEMENTOS, MSM EM OUTROS TERMOS
    
    
    lista_termos = ler.split()
    print(lista_termos)
    contador = 0
    for termo in lista_termos:
        if termo == 'Ola': ##CONTAGEM ESPECIFICA DOS ELEMENTOS/ TERMOS
            contador += 1
print(f'Contador de "Ol"= {contador}')


##MÉTODO JOIN, COLOCAR LISTAS DE PALAVRAS NUMA MSM STRING
minha_lista = ['Abacaxi', 'Limão', 'Maçã']

texto1 =  ', '.join(minha_lista) ##conectivo ',' depois de todo elemento da lista
with open(PASTA_DO_EXERCICIO / "texto1.txt", 'w', encoding='utf-8') as frase:
    frase.write(texto1)

texto2 = '\n'.join(minha_lista) ## \n dps de todo elemento
with open(PASTA_DO_EXERCICIO / "textos2.txt", 'w', encoding='utf-8') as frase:
    frase.write(texto2)
  

