import requests
import sqlite3
import validate_docbr as docbr
from operator import itemgetter
from Funções.Lista.Func import getInt
from Funções.Lista.Func import getFloat
import pandas as pd
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()


def listar_produtos():
    cursor.execute('SELECT * FROM produtos')
    data = {
        '   Código de Barras': [],
        '   Produto': [],
        '   Fabricante': []
    }
    for produto in cursor.fetchall():
        data['   Código de Barras'] += [produto[1]]
        data['   Produto'] += [produto[2]]
        data['   Fabricante'] += [produto[3]]
    print(pd.DataFrame(data))


def listar_clientes():
    cursor.execute('SELECT * FROM clientes')
    data = {
        '   Nome': [],
        '   CPF': [],
        '   CEP': [],
        '   Cidade': [],
        '   Estado': [],
        '   Rua': []
    }
    for cliente in cursor.fetchall():
        data['   Nome'] += [cliente[1]]
        data['   CPF'] += [cliente[2]]
        data['   CEP'] += [cliente[3]]
        data['   Cidade'] += [cliente[4]]
        data['   Estado'] += [cliente[5]]
        data['   Rua'] += [cliente[6]]
    print(pd.DataFrame(data))


def listar_vendas():
    cursor.execute('SELECT * FROM vendas')
    data = {
        '   Data': [],
        '   Hora': [],
        '   CPF do Cliente': [],
        '   Código de Barras': [],
        '   Quantidade': [],
        '   Valor Unitário': [],
        '   Valor Total': []
    }
    for venda in cursor.fetchall():
        data['   Data'] += [venda[1]]
        data['   Hora'] += [venda[2]]
        data['   CPF do Cliente'] += [venda[3]]
        data['   Código de Barras'] += [venda[4]]
        data['   Quantidade'] += [venda[5]]
        data['   Valor Unitário'] += [venda[6]]
        data['   Valor Total'] += [venda[7]]
    print(pd.DataFrame(data))


class Produto:
    def __init__(self, cod_barras, nome_produto=None, fabricante_produto=None):
        self.cob_barras = cod_barras
        self.nome_produto = nome_produto
        self.fabricante_produto = fabricante_produto

    def cadastrar_produto(self):
        cursor.execute('INSERT INTO produtos (cod_barras, nome_produto, fabricante_produto)'
                       'VALUES(?,?,?)', (self.cob_barras, self.nome_produto, self.fabricante_produto))

    def alterar_registro(self):
        cursor.execute(f'UPDATE produtos SET nome_produto=?, fabricante_produto=? WHERE cod_barras=?', (self.nome_produto, self.fabricante_produto, self.cob_barras))

    def excluir_registro(self):
        if input(f'Deseja deletar Produto? Essa ação é irreversível\n').lower() == 's':
            cursor.execute('DELETE FROM produtos WHERE cod_barras=?', (self.cob_barras,))
            print(f'Produto foi deletado')


class Cliente:
    def __init__(self, cpf_cliente, nome_cliente=None, cep_cliente=None):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.cep_cliente = cep_cliente
        endereco = requests.get(f'https://viacep.com.br/ws/{self.cep_cliente}/json/').json()
        self.cidade_cliente = endereco['localidade']
        self.estado_cliente = endereco['uf']
        self.rua_cliente = endereco['logradouro']

    def validar_cpf(self):
        docs = [(docbr.CPF, self.cpf_cliente)]
        return docbr.validate_docs(docs)[0]

    def cadastrar_cliente(self):
        if self.validar_cpf():
            cursor.execute('INSERT INTO clientes (nome_cliente, cpf_cliente, cep_cliente, cidade_cliente, estado_cliente, rua_cliente)'
                           'VALUES(?,?,?,?,?,?)', (self.nome_cliente, self.cpf_cliente, self.cep_cliente, self.cidade_cliente, self.estado_cliente, self.rua_cliente))

    def alterar_registro(self):
        if self.validar_cpf():
            cursor.execute(f'UPDATE clientes SET nome_cliente=? cep_cliente=?, cidade_cliente=?, estado_cliente=?, rua_cliente=? WHERE "id cliente"=?',
                           (self.nome_cliente, self.cep_cliente, self.cidade_cliente, self.estado_cliente, self.rua_cliente, self.cpf_cliente))

    def excluir_registro(self):
        if self.validar_cpf():
            if input(f'Deseja deletar Cliente? Essa ação é irreversível\n').lower() == 's':
                cursor.execute('DELETE FROM clientes WHERE id cpf_cliente=?', (self.cpf_cliente,))
                print(f'Cliente foi deletado')


class Vendas:
    def __init__(self, data_venda=None, hora_venda=None, cpf_cliente=None, cod_barras=None, quantidade:float=None, valor_unitario:float=None):
        self.data_venda = data_venda
        self.hora_venda = hora_venda
        self.cpf_cliente = cpf_cliente
        self.cod_barras = cod_barras
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = self.quantidade * self.valor_unitario

    def cadastrar_venda(self):
        cursor.execute('INSERT INTO vendas (data_venda, hora_venda, CPF_cliente, cod_barras, quantidade, valor_unitario, valor_total)'
                       'VALUES(?,?,?,?,?,?,?)', (self.data_venda, self.hora_venda, self.cpf_cliente, self.cod_barras, self.quantidade, self.valor_unitario, self.valor_total))

    def alterar_registro(self, id_venda):
        cursor.execute('UPDATE vendas SET data_venda=?, hora_venda=?, CPF_cliente=?, cod_barras=?, quantidade=?, '
                       'valor_unitario=?, valor_total=? WHERE id_venda=?', (self.data_venda, self.hora_venda,
                                                                            self.cpf_cliente, self.cod_barras,
                                                                            self.quantidade, self.valor_unitario,
                                                                            self.valor_total, id_venda))

    @staticmethod
    def excluir_registro(id_venda):
        if input(f'Deseja deletar Venda? Essa ação é irreversível\n').lower() == 's':
            cursor.execute('DELETE FROM vendas WHERE id_venda=?', (id_venda,))
            print(f'Venda foi deletada')


def rank_cliente():
    dic = {}
    cursor.execute('SELECT CPF_cliente FROM vendas')
    for cpf in cursor.fetchall():
        dic[cpf[0]] = cursor.execute('SELECT CPF_cliente FROM vendas').fetchall().count(cpf)
    new_dic = sorted(dic.items(), key=itemgetter(1), reverse=True)
    for i in new_dic:
        print(f'{i[0]} - {i[1]}')


def rank_produto():
    dic = {}
    cursor.execute('SELECT cod_barras FROM vendas')
    for cod in cursor.fetchall():
        dic[cod[0]] = cursor.execute('SELECT cod_barras FROM vendas').fetchall().count(cod)
    new_dic = sorted(dic.items(), key=itemgetter(1), reverse=True)
    for i in new_dic:
        print(f'{i[0]} - {i[1]}')


def listar_cpf():
    dic = {}
    cursor.execute('SELECT CPF_cliente FROM vendas')
    for cpf in cursor.fetchall():
        dic[cpf[0]] = []
    for i in cursor.execute('SELECT * FROM vendas').fetchall():
        dic[i[3]] += [i]
    for i in dic:
        print(f'\n{i} -')
        for j in dic[i]:
            print(j)


def listar_codigo():
    dic = {}
    cursor.execute('SELECT cod_barras FROM vendas')
    for cpf in cursor.fetchall():
        dic[cpf[0]] = []
    for i in cursor.execute('SELECT * FROM vendas').fetchall():
        dic[i[4]] += [i]
    for i in dic:
        print(f'\n{i} -')
        for j in dic[i]:
            print(j)


acoes = {'4': listar_cpf, '5': listar_codigo, '6': rank_produto, '7': rank_cliente}
while True:
    acao = input('Você deseja:\n'
                 '[1] Interagir com Produtos\n'
                 '[2] Interagir com Clientes\n'
                 '[3] Interagir com Vendas\n'
                 '[4] Listar as vendas por CPF\n'
                 '[5] Listar as vendas por Código de Barras\n'
                 '[6] Rankear as vendas por Produto\n'
                 '[7] Rnakear as vendas por Cliente\n').strip()
    if acao == '1':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 == '1':
            codigo = input('Informe o Código de Barras: ')
            nome = input('Informe o Nome do Produto: ')
            fabricante = input('Informe o Fabricante: ')
            Produto(codigo, nome, fabricante).cadastrar_produto()
        if acao2 == '2':
            listar_produtos()
            codigo = input('Informe o Código de Barras: ')
            nome = input('Informe o Nome do Produto: ')
            fabricante = input('Informe o Fabricante: ')
            Produto(codigo, nome, fabricante).alterar_registro()
        if acao2 == '3':
            listar_produtos()
            codigo = input('Informe o Código de Barras: ')
            Produto(codigo).excluir_registro()
        listar_produtos()
    elif acao == '2':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 == '1':
            nome = input('Informe o Nome do Cliente: ')
            cpf = input('Informe o CPF fo Cliente: ')
            cep = input('Informe o CEP fo Cliente: ')
            Cliente(cpf, nome, cep).cadastrar_cliente()
        if acao2 == '2':
            listar_clientes()
            nome = input('Informe o Nome do Cliente: ')
            cpf = input('Informe o CPF fo Cliente: ')
            cep = input('Informe o CEP fo Cliente: ')
            Cliente(cpf, nome, cep).alterar_registro()
        if acao2 == '3':
            listar_clientes()
            cpf = input('Informe o CPF fo Cliente: ')
            Cliente(cpf).excluir_registro()
        listar_clientes()
    elif acao == '3':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 == '1':
            data = input('Informe a Data da Venda: ')
            hora = input('Informe a Hora da Venda: ')
            cpf = input('Informe o CPF fo Cliente: ')
            codigo = input('Informe o Código de Barras: ')
            quantidade = getFloat('Informe a quantidade de produtos: ')
            valor_unitario = getFloat('Informe o valor unitário: ')
            Vendas(data, hora, cpf, codigo, quantidade, valor_unitario).cadastrar_venda()
        if acao2 == '2':
            listar_vendas()
            id_venda = getInt('Informe o id: ')
            data = input('Informe a Data da Venda: ')
            hora = input('Informe a Hora da Venda: ')
            cpf = input('Informe o CPF fo Cliente: ')
            codigo = input('Informe o Código de Barras: ')
            quantidade = getFloat('Informe a quantidade de produtos: ')
            valor_unitario = getFloat('Informe o valor unitário: ')
            Vendas(data, hora, cpf, codigo, quantidade, valor_unitario).alterar_registro(id_venda)
        if acao2 == '3':
            listar_vendas()
            Vendas().excluir_registro(getInt('Informe o id: '))
        listar_vendas()
    elif acao in '4567':
        acoes[acao]()
    conexao.commit()
    if input('Deseja parar? [S/N]\n').lower() == 's':
        break

cursor.close()
conexao.close()