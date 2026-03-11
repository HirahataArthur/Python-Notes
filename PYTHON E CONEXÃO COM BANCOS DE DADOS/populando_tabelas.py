import sqlite3 as conector

def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()

    criar = '''CREATE TABLE IF NOT EXISTS Produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL);'''

    criar2 = '''CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL);'''
    criar3 = '''CREATE TABLE IF NOT EXISTS Pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                data_pedido TEXT NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                FOREIGN KEY (produto_id) REFERENCES Produtos(id));'''

    cursor.execute(criar)
    cursor.execute(criar2)
    cursor.execute(criar3)

    conexao.commit()

def inserir_dados(conexao):
    cursor = conexao.cursor()

    produtos = [('Notebook', 2999.99, 108),
                ('Celular', 1500.00, 56),
                ('Tablet', 2000.99, 34)]
    
    clientes = [('Arthur', 'hirahataarthur@gmail.com'),
                ('Maria', 'marialuisa@gmail.com',)]
    
    pedidos = [(1,1,1, '2025-01-01'),
               (2,2,5, '2025-02-01'),
               (1,2,10, '2025-03-01')]
    cursor.executemany('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)',produtos)
    cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)',clientes)
    cursor.executemany('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)',pedidos)
    conexao.commit()
    cursor.close()
    
def deletar_dados(conexao):
    cursor = conexao.cursor()

    deletar = '''DELETE FROM Clientes WHERE email='marialuiza@gmail.com' '''
    cursor.execute(deletar)
    conexao.commit()
    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco('mercadinho.db')
    criar_tabela(conexao)
    inserir_dados(conexao)
    deletar_dados(conexao)
    conexao.close()

    

