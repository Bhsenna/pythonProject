import requests
import sqlite3
import validate_docbr as docbr
from operator import itemgetter
from Funções.Lista.Func import getInt
from Funções.Lista.Func import getFloat
import pandas as pd
import barcodenumber
import arrow

pd.set_option('display.max_columns', 14)
pd.set_option('display.width', 200)

conexao = sqlite3.connect('Voos.db')
cursor = conexao.cursor()


def listar_Aeronaves():
    cursor.execute('SELECT * FROM Aeronaves')
    data = {
        '   Código': [],
        '   Modelo': [],
        '   Assentos Disponíveis': [],
        '   Limite Bagagem (Kg)': []
    }
    for aeronave in cursor.fetchall():
        data['   Código'] += [aeronave[0]]
        data['   Modelo'] += [aeronave[1]]
        data['   Assentos Disponíveis'] += [aeronave[2]]
        data['   Limite Bagagem (Kg)'] += [aeronave[3]]
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


def listar_Empresas():
    cursor.execute('SELECT * FROM Empresas_Aereas')
    data = {
        '   Código': [],
        '   Nome': [],
        '   Nacionalidade': [],
        '   Sigla': []
    }
    for aeronave in cursor.fetchall():
        data['   Código'] += [aeronave[0]]
        data['   Nome'] += [aeronave[1]]
        data['   Nacionalidade'] += [aeronave[2]]
        data['   Sigla'] += [aeronave[3]]
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


def listar_Aeroportos():
    cursor.execute('SELECT * FROM Aeroportos')
    data = {
        '   Código': [],
        '   Nome': [],
        '   Sigla': [],
        '   Cidade': [],
        '   Estado': [],
        '   País': [],
        '   Continente': []
    }
    for aeronave in cursor.fetchall():
        data['   Código'] += [aeronave[0]]
        data['   Nome'] += [aeronave[1]]
        data['   Sigla'] += [aeronave[2]]
        data['   Cidade'] += [aeronave[3]]
        data['   Estado'] += [aeronave[4]]
        data['   País'] += [aeronave[5]]
        data['   Continente'] += [aeronave[6]]
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


def listar_Voos():
    cursor.execute('SELECT * FROM Aeroportos')
    data = {
        '   Código': [],
        '   Data/Saída': [],
        '   Hora/Saída': [],
        '   Aeroporto Decolagem': [],
        '   Aeroporto Destino': [],
        '   Empresa': [],
        '   N° Passageiros': [],
        '   Assentos Disponíveis': [],
        '   Carga Carregada (Kg)': [],
        '   Aeronave': [],
        '   Data/Chegada': [],
        '   Hora/Chegada': [],
        '   Natureza Voo': []
    }
    for aeronave in cursor.fetchall():
        data['   Código'] += [aeronave[0]]
        data['   Data/Saída'] += [aeronave[1]]
        data['   Hora/Saída'] += [aeronave[2]]
        data['   Aeroporto Decolagem'] += [aeronave[3]]
        data['   Aeroporto Destino'] += [aeronave[4]]
        data['   Empresa'] += [aeronave[5]]
        data['   N° Passageiros'] += [aeronave[6]]
        data['   Assentos Disponíveis'] += [aeronave[7]]
        data['   Carga Carregada (Kg)'] += [aeronave[8]]
        data['   Aeronave'] += [aeronave[9]]
        data['   Data/Chegada'] += [aeronave[10]]
        data['   Hora/Chegada'] += [aeronave[11]]
        data['   Natureza Voo'] += [aeronave[12]]
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


class Aeronaves:
    def __init__(self, cod_aeronave, modelo=None, assentos_disponiveis: int = None, limite_bagagem: int = None):
        self.cod_aeronave = cod_aeronave
        self.modelo = modelo
        self.assentos_disponiveis = assentos_disponiveis
        self.limite_bagagem = limite_bagagem

    def cadastrar(self):
        try:
            cursor.execute('INSERT INTO Aeronaves (cod_aeronave, modelo, assentos_disponiveis, limite_bagagem(kg))'
                           'VALUES(?,?,?,?)',
                           (self.cod_aeronave, self.modelo, self.assentos_disponiveis, self.limite_bagagem))
        except sqlite3.IntegrityError:
            print('Código de Aeronave já está cadastrado\n')

    def alterar(self):
        opcoes = ["modelo", "assentos_disponiveis", "limite_bagagem(kg)"]
        escolha = getInt(
            'Você deseja alterar:\n[0] Modelo da Aeronave\n[1] Número de assentos disponíveis\n[2] Limite de Bagagem(kg)')
        novo_valor = input('Informe o novo valor: ')
        cursor.execute(f'UPDATE Aeronaves SET {opcoes[escolha]}=? WHERE cod_aeronave=?',
                       (novo_valor, self.cod_aeronave))

    def excluir(self):
        if input(f'Deseja deletar Aeronave? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM Aeronave WHERE cod_aeronave=?', (self.cod_aeronave,))
            cursor.execute('DELETE FROM Voos WHERE cod_aeronave=?', (self.cod_aeronave,))
            print(f'Aeronave foi deletada')


class Empresas:
    def __init__(self, cod_empresa, nome_empresa=None, nacionalidade=None, sigla_empresa=None):
        self.cod_empresa = cod_empresa
        self.nome_empresa = nome_empresa
        self.nacionalidade = nacionalidade
        self.sigla_empresa = sigla_empresa

    def cadastrar(self):
        try:
            cursor.execute('INSERT INTO Empresas_Aereas (cod_empresa, nome_empresa, nacionalidade, sigla_empresa)'
                           'VALUES(?,?,?,?)',
                           (self.cod_empresa, self.nome_empresa, self.nacionalidade, self.sigla_empresa))
        except sqlite3.IntegrityError:
            print('Código de Empresa já está cadastrado\n')

    def alterar(self):
        opcoes = ["nome_empresa", "nacionalidade", "sigla_empresa"]
        escolha = getInt(
            'Você deseja alterar:\n[0] Nome da Empresa\n[1] Nacionalidade da Empresa\n[2] Sigla da Empresa\n')
        novo_valor = input('Informe o novo valor: ')
        cursor.execute(f'UPDATE Empresas_Aereas SET {opcoes[escolha]}=? WHERE cod_empresa=?',
                       (novo_valor, self.cod_empresa))

    def excluir(self):
        if input(f'Deseja deletar Empresa? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM Empresas_Aereas WHERE cod_empresa=?', (self.cod_empresa,))
            cursor.execute('DELETE FROM Voos WHERE cod_empresa=?', (self.cod_empresa,))
            print(f'Empresa foi deletada')


class Aeroportos:
    def __init__(self, cod_aeroporto, nome_aeroporto=None, sigla_aeroporto=None, cidade=None, estado=None, pais=None,
                 continente=None):
        self.cod_aeroporto = cod_aeroporto
        self.nome_aeroporto = nome_aeroporto
        self.sigla_aeroporto = sigla_aeroporto
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.continente = continente

    def cadastrar(self):
        try:
            cursor.execute(
                'INSERT INTO Aeroportos (cod_aeroporto, nome_aeroporto, sigla_aeroporto, cidade, estado, pais, continente)'
                'VALUES(?,?,?,?,?,?,?)', (
                    self.cod_aeroporto, self.nome_aeroporto, self.sigla_aeroporto, self.cidade, self.estado, self.pais,
                    self.continente))
        except sqlite3.IntegrityError:
            print('Código de Aeroporto já está cadastrado\n')

    def alterar(self):
        opcoes = ["nome_aeroporto", "sigla_aeroporto", "cidade", "estado", "pais", "continente"]
        escolha = getInt(
            'Você deseja alterar:\n[0] Nome do Aeroporto\n[1] Sigla do Aeroporto\n[2] Cidade\n[3] Estado\n[4] País\n[5] Continente\n')
        novo_valor = input('Informe o novo valor: ')
        cursor.execute(f'UPDATE Aeroportos SET {opcoes[escolha]}=? WHERE cod_aeroporto=?',
                       (novo_valor, self.cod_aeroporto))

    def excluir(self):
        if input(f'Deseja deletar Aeroporto? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM Aeroportos WHERE cod_aeroporto=?', (self.cod_aeroporto,))
            cursor.execute('DELETE FROM Voos WHERE cod_aeroporto=?', (self.cod_aeroporto,))
            print(f'Aeroporto foi deletada')


class Voos:
    def __init__(self, cod_voo, data_saida=None, hora_saida=None, cod_aeroporto_decolagem=None,
                 cod_aeroporto_destino=None, cod_empresa=None, num_passageiros: int = None,
                 assentos_disponiveis: int = None,
                 carga_carregada: float = None, cod_aeronave=None, data_chegada=None, hora_chegada=None,
                 natureza_voo=None):
        self.cod_voo = cod_voo
        self.data_saida = data_saida
        self.hora_saida = hora_saida
        self.cod_aeroporto_decolagem = cod_aeroporto_decolagem
        self.cod_aeroporto_destino = cod_aeroporto_destino
        self.cod_empresa = cod_empresa
        self.num_passageiros = num_passageiros
        self.assentos_disponiveis = assentos_disponiveis
        self.carga_carregada = carga_carregada
        self.cod_aeronave = cod_aeronave
        self.data_chegada = data_chegada
        self.hora_chegada = hora_chegada
        self.natureza_voo = natureza_voo

    def cadastrar(self):
        try:
            cursor.execute('INSERT INTO Aeroportos (cod_voo, data_saida, hora_saida, cod_aeroporto_decolagem, '
                           'cod_aeroporto_destino, cod_empresa, num_passageiros, assentos_disponiveis, '
                           'carga_carregada(kg), cod_aeronave, data_chegada, hora_chegada, natureza_voo)'
                           'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                           (self.cod_voo, self.data_saida, self.hora_saida, self.cod_aeroporto_decolagem,
                            self.cod_aeroporto_destino, self.cod_empresa, self.num_passageiros,
                            self.assentos_disponiveis, self.carga_carregada, self.cod_aeronave,
                            self.data_chegada, self.hora_chegada, self.natureza_voo))
        except sqlite3.IntegrityError:
            print('Código de Voo já está cadastrado\n')

    def alterar(self):
        opcoes = ["data_saida", "hora_saida", "cod_aeroporto_decolagem", "cod_aeroporto_destino",
                  "cod_empresa", "num_passageiros", "assentos_disponiveis", "carga_carregada(kg)",
                  "cod_aeronave", "data_chegada", "hora_chegada", "natureza_voo"]
        escolha = getInt(
            'Você deseja alterar:\n[0] Data de Saída\n[1] Hora de Saída\n[2] Aeroporto de Decolagem'
            '\n[3] Aeroporto de Destino\n[4] Empresa do Voo\n[5] Número de Passageiros'
            '\n[6] Qtd de Assentos Disponíveis\n[7] Carga Carregada (kg)\n[8] Código da Aeronave'
            '\n[9] Data de Chegada\n[10] Hora de Chegada\n[11] Natureza do Voo\n')
        novo_valor = input('Informe o novo valor: ')
        cursor.execute(f'UPDATE Voos SET {opcoes[escolha]}=? WHERE cod_voo=?',
                       (novo_valor, self.cod_voo))

    def excluir(self):
        if input(f'Deseja deletar Voo? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM Voos WHERE cod_voo=?', (self.cod_voo,))
            print(f'Voo foi deletada')


dic1 = {'1': Aeronaves, '2': Empresas, '3': Aeronaves, '4': Voos}
while True:
    acao = input('Você deseja:\n'
                 '[1] Interagir com Aeronaves\n'
                 '[2] Interagir com Empresas\n'
                 '[3] Interagir com Aeronaves\n'
                 '[4] Interagir com Voos\n').strip()
    acao2 = input('Você deseja:\n'
                  f'[1] Cadastrar {dic1[acao]}\n'
                  f'[2] Editar {dic1[acao]}\n'
                  f'[3] Deletar {dic1[acao]}\n').strip()
    if acao == '1':
        pass
    conexao.commit()
    if input('Deseja parar? [S/N]\n').lower().startswith('s'):
        break

cursor.close()
conexao.close()
