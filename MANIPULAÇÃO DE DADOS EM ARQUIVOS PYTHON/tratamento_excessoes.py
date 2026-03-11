##TENTATIVA DE CRIAR ARQUIVO JA EXISTENTE
try:
    with open("arquivo.txt", 'x') as arquivo:
        arquivo.write("Conteudo")
except FileExistsError:
    print("Arquivo ja existe!") 

##TENTATIVA DE ABRIR ARQUIVO NAO EXISTENTE
try: 
    with open("arquivo_imaginario.txt", 'r') as arquivo:
        conteudo = arquivo.read()   
except FileNotFoundError:
    print("Arquivo não encontrado")