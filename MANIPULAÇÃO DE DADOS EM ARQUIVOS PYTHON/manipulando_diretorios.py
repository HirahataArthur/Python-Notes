##CRIAÇÃO DE DIRETORIOS
import os
def create():
    try:
        os.mkdir(str(input("Digite o nome do novo diretorio >>>  ")))
    except Exception as e:
        print(f"erro encontrado: {e}")


##REMOÇÃO DE DIRETORIOS
def remove():
    try:
        os.rmdir(str(input("Insira o nome do diretório a ser excluido \n(lembre-se de não excluir diretorios vazios)\n>>> ")))
    except Exception as e:
        print(f"Erro encontrado: {e}")

##LISTAR DIRETORIOS
def lista():
    with os.scandir('Nao interessante') as entries:
        print("Listando os compotentes do diretorio: ")
        for entry in entries:
            
            print(f" >> {entry.name} é arquivo? ", entry.is_file()) ##ANALISAR ENTRIES [ .name .is_dir() .is_file() .stat() ]

##PARA QUALQUER UMA DAS FUNÇÕES FUNCIONAREM LEMBRE DE CHAMAR ELAS (lista() remove()....)
lista()