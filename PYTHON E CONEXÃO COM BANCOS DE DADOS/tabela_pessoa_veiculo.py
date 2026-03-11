import sqlite3 
def  conectar_banco(nome_banco): ##função pra criar conexão com o banco de dados
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao): ##função para criar tabelas
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa ( 
                   cpf INTEGER NOT NULL,
                   nome TEXT NOT NULL,
                   idade INTEGER NOT NULL,
                   nascimento DATE NOT NULL,
                   PRIMARY KEY (cpf))''') ##cria as tabelas no banco de dados
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS Marca ( id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id));''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo ( placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL, cor TEXT NOT NULL,
                    proprietario INTEGER NOT NULL, marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id));''') 
    conexao.commit() ##ENVIAR ALTERAÇÕES

if __name__ == '__main__':
    conexao = conectar_banco('meu_banco2.db')
    criar_tabelas(conexao)
    conexao.close()