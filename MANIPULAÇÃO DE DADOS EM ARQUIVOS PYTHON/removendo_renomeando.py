##MÉTODO 'REMOVE' E 'RENAME'

##FUNÇÃO REMOVE:
import os       
arquivo_a_remover = "arquivo_a_remover.txt" ##eu executei o codigo ent esse arquivo ja nao existe mais kkkkk

try:
    os.remove(arquivo_a_remover)
    print(f"O arquivo '{arquivo_a_remover}' foi removido")
except FileNotFoundError:
    print(f"Arquivo '{arquivo_a_remover}' nao encontrado")
except Exception as e:
    print(f"Ocorreu um erro ao remover o arquivo: {e}")  

##MÉTODO RENAME

old_name_typin = str(input("Insira o nome do arquivo a renomear: "))
old_name =  old_name_typin + '.txt'
new_name_typin = str(input("Insira o nome do novo arquivo: "))
new_name = new_name_typin + '.txt'

try:
    os.rename(old_name, new_name)
    print(f"O arquivo '{old_name}' teve seu nome alterado para '{new_name}'")
except FileNotFoundError:
    print(f"Arquivo '{old_name}' não encontrado.")
