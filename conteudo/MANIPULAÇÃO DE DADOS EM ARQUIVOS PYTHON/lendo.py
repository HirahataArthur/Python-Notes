import os
print("Diretório atual:", os.getcwd()) ##para saber que diretorio o terminal aponta parta ler

with open("dados.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("dados.txt", 'a') as arquivo1:
    arquivo1.write("boiola ")
    arquivo1.close()


# this code snippet opens a text file named "dados.txt" in read mode, reads its content, and prints it to the console. It then opens the same file in append mode and adds the string "boiola " to the end of the file. Finally, it closes the file after writing. However , it is important to note that the file "dados.txt" must exist in the current working directory for this code to work correctly. If the file does not exist, an error will occur when trying to open it in read mode.
