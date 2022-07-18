import sqlite3

conexao = sqlite3.connect('Banco de dados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'cpf TEXT,'
               'nome TEXT,'
               'data_nascimento TEXT,'
               'cep TEXT,'
               'peso REAL,'
               'altura REAL)')
conexao.commit()
cpf = input('Digite o CPF: ')
nome = input('Digite o nome: ')
data_nascimento = input('Digite a Data de Nascimento: ')
cep = input('Digite o CEP: ')
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

cursor.execute('INSERT INTO clientes (cpf, nome, data_nascimento, cep, peso, altura)'
               'VALUES(?,?,?,?,?,?)', (cpf, nome, data_nascimento, cep, peso, altura))
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for cliente in cursor.fetchall():
    print(f'{cliente[0]} - {cliente[1]} - {cliente[2]} - {cliente[3]} - {cliente[4]} - {cliente[5]} - {cliente[6]}')

cursor.close()
conexao.close()