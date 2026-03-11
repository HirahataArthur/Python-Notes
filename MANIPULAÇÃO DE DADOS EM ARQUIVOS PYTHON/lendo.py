import os
print("Diretório atual:", os.getcwd()) ##para saber que diretorio o terminal aponta parta ler

with open("dados.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("dados.txt", 'a') as arquivo1:
    arquivo1.write("boiola ")
    arquivo1.close()



