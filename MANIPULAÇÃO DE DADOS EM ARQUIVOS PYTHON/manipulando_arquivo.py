import os

arquivo = open("olamundo.txt")
abs = os.path.abspath("olamundo.txt")
while True:
    print(f"------------------------MANIPULANDO ARQUIVOS--------------- \n ARQUIVO ATUAL: {arquivo.name} \n CAMINHO ABSOLUTO DO ARQUIVO: {abs}") 
    print(" DIGITE [1] - LER ARQUIVO   \n DIGITE [2] - RESCREVER NO ARQUIVO \n DIGITE [3] - ADICIONAR AO ARQUIVO \n DIGITE [4] - SAIR")


    opc = int(input("-->"))    
    if opc == 1:
        with open("olamundo.txt", 'r') as arquivoR:
            conteudo = arquivoR.read()
            print(f"CONTEÚDO EXISTENTE: {conteudo}")

            
    elif opc == 2:
        with open("olamundo.txt", 'w') as arquivoE:
           msg = str(input("Mensagem: "))
           arquivoE.write(msg)


    elif opc == 3:
        with open("olamundo.txt", 'r') as arquivoR:
            conteudo = arquivoR.read()
            print(f"CONTEÚDO EXISTENTE: {conteudo}")
        with open("olamundo.txt", 'a') as arquivoA:
            msg = str(input("CONTEÚDO A ADICIONAR: "))
            arquivoA.write(msg)


    elif opc == 4:
        print("saindo...")
        break
    else:
        print("Opção inexistente")