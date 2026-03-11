import sqlite3 as conector


## Usaremos comandos como DELETE  e UPDATE


## Abrir conexao
conexao = conector.connect('meu_banco2.db')
conexao.execute("PRAGMA foreign_keys = on") ## trabalhar respeitando chaves estrangeiras
cursor = conexao.cursor()

## Alterar ou Atualizar dados
comando1 = '''UPDATE Pessoa SET idade= 19 WHERE cpf=59580492832;''' ## Aplica a alteração se orientando pelo cpf 
cursor.execute(comando1)

## Para deletar
comando2 = '''DELETE FROM Pessoa WHERE cpf=59580492832;'''
cursor.execute(comando2)

## Enviar Alteração
conexao.commit()

## Fechar conexoes
cursor.close()
conexao.close()