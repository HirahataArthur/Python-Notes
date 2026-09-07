import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("meu_banco2.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa WHERE idade=18;''' ##SELECIONANDO APENAS INDIVIDUOS QUE TENHAM ESSA CONDIÇÃO (18 ANOS)
cursor.execute(comando, {"idade":18})

registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf: ", type(pessoa.cpf), pessoa.cpf)
    print("nome: ", type(pessoa.nome), pessoa.nome)
    print("nascimento: ", type(pessoa.data_nascimento), pessoa.data_nascimento)

## Fechar conexão
cursor.close()
conexao.close()
