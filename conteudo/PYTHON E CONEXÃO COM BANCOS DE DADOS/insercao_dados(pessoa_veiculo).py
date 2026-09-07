##Uso do comando INSERT INTO 
import sqlite3 as conector

##mesmo processo de antes....

## Abertura da conexão e aquisição de cursor
conexao = conector.connect('meu_banco2.db')
cursor = conexao.cursor()
cpf = int(input('Insira seu cpf: '))
nome = str(input('Insira seu nome: '))
idade = int(input("Insira sua idade: "))
##EXECUÇÃO DE UM COMANDO
comando = f'''INSERT INTO Pessoa (cpf, nome, idade, nascimento)
            VALUES ({cpf}, '{nome}', {idade}, '2006-01-11');'''
cursor.execute(comando)

##EFETUAR ALTERAÇÕES
conexao.commit()

##FECHAR CONEXOES
cursor.close()
conexao.close()