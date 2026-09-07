import os

arquivo1 = open("olamundo.txt", 'w')
print("CAMINHO ABSOLUTO:", os.path.abspath(arquivo1.name))  # caminho absoluto
arquivo1.write("pouha!")            # escreve no arquivo
arquivo1.close()                        # fecha e grava no disco

print("CAMINHO RELATVO: ", os.path.relpath(arquivo1.name)) #escreve caminho relativo
print("INFO DO ARQUIVO:", arquivo1)