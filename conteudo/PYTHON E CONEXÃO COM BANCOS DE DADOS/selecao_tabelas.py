import sqlite3 as conector

## Abrir conexao
conexao = conector.connect('meu_banco2.db')
cursor = conexao.cursor()

## Seleção da tabela

comando = '''SELECT nome, idade FROM Pessoa;'''
cursor.execute(comando)

## Recuperando os dados
registros = cursor.fetchall()   
print("Tipo retornado pelo fetchall():", type(registros))

for registro in registros:
    print(f"Tipo: {type(registro)} -  Conteúdo: {registro}")


##fechar conexao
cursor.close()
conexao.close()
