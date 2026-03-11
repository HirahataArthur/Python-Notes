import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("meu_banco2.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa'''
cursor.execute(comando)

registro_pessoas = cursor.fetchall()
for registro in registro_pessoas:
    pessoa = Pessoa(*registro)
    print(f"NOME: {pessoa.nome} - IDADE: {pessoa.idade} - NASCIMENTO: {pessoa.data_nascimento}")

cursor.close()
conexao.close()