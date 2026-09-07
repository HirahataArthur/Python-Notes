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

# this code snippet provides functions to create, remove, and list directories using the os module in Python. The create() function prompts the user for a directory name and attempts to create it, handling any exceptions that may occur. The remove() function prompts for a directory name to delete, ensuring it is empty before removal. The lista() function lists the contents of a specified directory, indicating whether each entry is a file or not. To use any of these functions, they must be called explicitly in the code. However, the current implementation of the lista() function is hardcoded to scan a directory named 'Nao interessante', which may not exist, leading to potential errors.