import sqlite3 as conector
from modelo import Pessoa ##importar o modelo Pessoa para agilizar

##msm esquema... Abrir conexao...
conexao = conector.connect('meu_banco2.db')
cursor = conexao.cursor()

##Criar objeto 'Pessoa'

pessoa = Pessoa(59480392731, 'Naomi', 21,'2004-10-01')

comando = '''
            INSERT INTO Pessoa (cpf, nome, idade,nascimento)
            VALUES (?, ?, ?, ?);''' ##NAO PASSA VALORES, COLOCA '?' ONDE SERIAM PASSADOS

cursor.execute(comando, (pessoa.cpf, 
                         pessoa.nome,
                         pessoa.idade,
                         pessoa.data_nascimento)) ##NA HORA DE EXECUTAR PASSA 'comando' e substitui valores que 
                                                ##- seriam enviados por cpf, nome, nascimento

## Enviar alterações
conexao.commit()

## Fechar conexoes
cursor.close()
conexao.close() 

