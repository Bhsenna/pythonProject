import requests
import sqlite3
import validate_docbr as docbr
from operator import itemgetter
from Funções.Lista.Func import getInt
from Funções.Lista.Func import getFloat
import pandas as pd
import barcodenumber
import arrow

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
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


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
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


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
        data['   Valor Unitário'] += [f'{venda[6]:.2f}']
        data['   Valor Total'] += [f'{venda[7]:.2f}']
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


def validar_cpf(cpf_cliente):
    docs = [(docbr.CPF, cpf_cliente)]
    if cpf_cliente in cpfs:
        existe = True
    else:
        existe = False
    return docbr.validate_docs(docs)[0] and existe


def validar_codigo(codigo: str):
    return barcodenumber.check_code('ean13', codigo)


class Produto:
    def __init__(self, cod_barras, nome_produto=None, fabricante_produto=None):
        self.cob_barras = cod_barras
        self.nome_produto = nome_produto
        self.fabricante_produto = fabricante_produto

    def cadastrar_produto(self):
        try:
            cursor.execute('INSERT INTO produtos (cod_barras, nome_produto, fabricante_produto)'
                           'VALUES(?,?,?)', (self.cob_barras, self.nome_produto, self.fabricante_produto))
        except sqlite3.IntegrityError:
            print('Código de Barras já está cadastrado\n')

    def alterar_registro(self):
        opcoes = ["nome_produto", "fabricante_produto"]
        escolha = getInt('Você deseja alterar:\n[0] Nome do Produto\n[1] Fabricante do Produto\n')
        novo_valor = input('Informe o novo valor: ')
        cursor.execute(f'UPDATE produtos SET {opcoes[escolha]}=? WHERE cod_barras=?', (novo_valor, self.cod_barras))

    def excluir_registro(self):
        if input(f'Deseja deletar Produto? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM produtos WHERE cod_barras=?', (self.cob_barras,))
            cursor.execute('DELETE FROM vendas WHERE cod_barras=?', (self.cob_barras,))
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

    def cadastrar_cliente(self):
        try:
            cursor.execute('INSERT INTO clientes (nome_cliente, cpf_cliente, cep_cliente, '
                           'cidade_cliente, estado_cliente, rua_cliente)'
                           'VALUES(?,?,?,?,?,?)', (self.nome_cliente, self.cpf_cliente, self.cep_cliente,
                                                   self.cidade_cliente, self.estado_cliente, self.rua_cliente))
        except sqlite3.IntegrityError:
            print('CPF já está cadastrado\n')

    def alterar_registro(self):
        if self.validar_cpf():
            opcoes = ["nome_cliente", "cep_cliente"]
            escolha = getInt('Você deseja alterar:\n[0] Nome do Cliente\n[1] CEP do Cliente\n')
            novo_valor = input('Informe o novo valor: ')
            if escolha == 1:
                endereco = requests.get(f'https://viacep.com.br/ws/{novo_valor}/json/').json()
                cidade_cliente = endereco['localidade']
                estado_cliente = endereco['uf']
                rua_cliente = endereco['logradouro']
                cursor.execute(f'UPDATE clientes SET cep_cliente=?, cidade_cliente=?, estado_cliente=?, rua_cliente=? WHERE cpf_cliente=?',
                               (novo_valor[escolha], cidade_cliente, estado_cliente, rua_cliente, self.cpf_cliente))
            else:
                cursor.execute(f'UPDATE clientes SET {opcoes[escolha]}=? WHERE cpf_cliente=?', (novo_valor, self.cpf_cliente))

    def excluir_registro(self):
        if input(f'Deseja deletar Cliente? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM clientes WHERE cpf_cliente=?', (self.cpf_cliente,))
            cursor.execute('DELETE FROM vendas WHERE CPF_cliente=?', (self.cpf_cliente,))
            print(f'Cliente foi deletado')


class Vendas:
    def __init__(self, data_venda=None, hora_venda=None, cpf_cliente=None,
                 cod_barras=None, quantidade: float = None, valor_unitario: float = None):
        self.data_venda = data_venda
        self.hora_venda = hora_venda
        self.cpf_cliente = cpf_cliente
        self.cod_barras = cod_barras
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        if self.valor_unitario is not None and self.quantidade is not None:
            self.valor_total = self.quantidade * self.valor_unitario

    def cadastrar_venda(self):
        cursor.execute(
            'INSERT INTO vendas (data_venda, hora_venda, CPF_cliente, '
            'cod_barras, quantidade, valor_unitario, valor_total)'
            'VALUES(?,?,?,?,?,?,?)', (self.data_venda, self.hora_venda, self.cpf_cliente,
                                      self.cod_barras, self.quantidade, self.valor_unitario, self.valor_total))

    @staticmethod
    def alterar_registro(id_venda):
        opcoes = ["data_venda", "hora_venda", "CPF_cliente", "cod_barras", "quantidade", "valor_unitario"]
        escolha = getInt('Você deseja alterar:\n[0] Data da Venda\n[1] Hora da Venda\n[2] CPF do Cliente\n[3] Código de Barras\n[4] Quantidade\n[5] Valor Unitário\n')
        novo_valor = input('Informe o novo valor: ')
        cursor.execute(f'UPDATE vendas SET {opcoes[escolha]}=? WHERE id_venda=?', (novo_valor, id_venda))

    @staticmethod
    def excluir_registro(id_venda):
        if input(f'Deseja deletar Venda? Essa ação é irreversível [S/N]\n').lower().startswith('s'):
            cursor.execute('DELETE FROM vendas WHERE id_venda=?', (id_venda,))
            print(f'Venda foi deletada')


def rank_cliente():
    data = {
        '   Cliente (CPF)': [],
        '   Valor (R$)': []
    }
    dic = {}
    cursor.execute('SELECT * FROM vendas')
    for venda in cursor.fetchall():
        dic[f'{venda[3]}'] = 0
    for venda in cursor.execute('SELECT * FROM vendas').fetchall():
        dic[f'{venda[3]}'] += venda[7]
    new_dic = sorted(dic.items(), key=itemgetter(1), reverse=True)
    for i in new_dic:
        data['   Cliente (CPF)'] += [i[0]]
        data['   Valor (R$)'] += [f'{i[1]:.2f}']
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


def rank_produto():
    data = {
        '   Código de Barras': [],
        '   Valor (R$)': []
    }
    dic = {}
    cursor.execute('SELECT * FROM vendas')
    for venda in cursor.fetchall():
        dic[f'{venda[4]}'] = 0
    for venda in cursor.execute('SELECT * FROM vendas').fetchall():
        dic[f'{venda[4]}'] += venda[7]
    new_dic = sorted(dic.items(), key=itemgetter(1), reverse=True)
    for i in new_dic:
        data['   Código de Barras'] += [i[0]]
        data['   Valor (R$)'] += [f'{i[1]:.2f}']
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas')
    else:
        print(data_frame)


def listar_cpf(cpf):
    data = {
        '   Data': [],
        '   Hora': [],
        '   CPF do Cliente': [],
        '   Código de Barras': [],
        '   Quantidade': [],
        '   Valor Unitário': [],
        '   Valor Total': []
    }
    cursor.execute('SELECT * FROM vendas')
    for venda in cursor.fetchall():
        if venda[3] == cpf:
            data['   Data'] += [venda[1]]
            data['   Hora'] += [venda[2]]
            data['   CPF do Cliente'] += [venda[3]]
            data['   Código de Barras'] += [venda[4]]
            data['   Quantidade'] += [venda[5]]
            data['   Valor Unitário'] += [f'{venda[6]:.2f}']
            data['   Valor Total'] += [f'{venda[7]:.2f}']
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas sobre esse CPF')
    else:
        print(data_frame)


def listar_codigo(codigo):
    data = {
        '   Data': [],
        '   Hora': [],
        '   CPF do Cliente': [],
        '   Código de Barras': [],
        '   Quantidade': [],
        '   Valor Unitário': [],
        '   Valor Total': []
    }
    cursor.execute('SELECT * FROM vendas')
    for venda in cursor.fetchall():
        if venda[4] == codigo:
            data['   Data'] += [venda[1]]
            data['   Hora'] += [venda[2]]
            data['   CPF do Cliente'] += [venda[3]]
            data['   Código de Barras'] += [venda[4]]
            data['   Quantidade'] += [venda[5]]
            data['   Valor Unitário'] += [f'{venda[6]:.2f}']
            data['   Valor Total'] += [f'{venda[7]:.2f}']
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há vendas registradas sobre esse Código')
    else:
        print(data_frame)


acoes = {'4': listar_cpf, '5': listar_codigo, '6': rank_produto, '7': rank_cliente}
while True:
    cpfs = []
    cursor.execute('SELECT cpf_cliente FROM clientes')
    for i in cursor.fetchall():
        cpfs.append(i[0])
    codigos = []
    cursor.execute('SELECT cod_barras FROM produtos')
    for i in cursor.fetchall():
        codigos.append(i[0])
    acao = input('Você deseja:\n'
                 '[1] Interagir com Produtos\n'
                 '[2] Interagir com Clientes\n'
                 '[3] Interagir com Vendas\n'
                 '[4] Listar as vendas por CPF\n'
                 '[5] Listar as vendas por Código de Barras\n'
                 '[6] Rankear as vendas por Produto\n'
                 '[7] Rankear as vendas por Cliente\n').strip()
    if acao == '1':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 == '1':
            codigo = input('Informe o Código de Barras: ')
            while not validar_codigo(codigo):
                codigo = input('Insira um Código de Barras valido: ')
            nome = input('Informe o Nome do Produto: ')
            fabricante = input('Informe o Fabricante: ')
            Produto(codigo, nome, fabricante).cadastrar_produto()
        if acao2 == '2':
            listar_produtos()
            codigo = input('Informe o Código de Barras: ')
            while codigo not in codigos:
                codigo = input('Insira um Código de Barras valido: ')
            Produto(codigo, None, None).alterar_registro()
        if acao2 == '3':
            listar_produtos()
            codigo = input('Informe o Código de Barras: ')
            while codigo not in codigos:
                codigo = input('Insira um Código de Barras valido: ')
            Produto(codigo).excluir_registro()
        listar_produtos()
    elif acao == '2':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 == '1':
            cpf = input('Informe o CPF do Cliente: ').replace('-', '').replace('.', '')
            docs = [(docbr.CPF, cpf)]
            while not docbr.validate_docs(docs)[0]:
                cpf = input('Insira um CPF valido: ').replace('-', '').replace('.', '')
                docs = [(docbr.CPF, cpf)]
            nome = input('Informe o Nome do Cliente: ')
            cep = input('Informe o CEP do Cliente: ').replace('-', '')
            Cliente(cpf, nome, cep).cadastrar_cliente()
        if acao2 == '2':
            listar_clientes()
            cpf = input('Informe o CPF do Cliente: ').replace('-', '').replace('.', '')
            while not validar_cpf(cpf):
                cpf = input('Insira um CPF valido: ').replace('-', '').replace('.', '')
            Cliente(cpf, None, None).alterar_registro()
        if acao2 == '3':
            listar_clientes()
            cpf = input('Informe o CPF fo Cliente: ')
            while not validar_cpf(cpf):
                cpf = input('Insira um CPF valido: ').replace('-', '').replace('.', '')
            Cliente(cpf).excluir_registro()
        listar_clientes()
    elif acao == '3':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 == '1':
            data = arrow.now().format('DD/MM/YYYY')
            hora = arrow.now().format('HH:mm')
            cpf = input('Informe o CPF do Cliente: ').replace('-', '').replace('.', '')
            while cpf not in cpfs:
                cpf = input('Insira um CPF valido: ').replace('-', '').replace('.', '')
            codigo = input('Informe o Código de Barras: ')
            while codigo not in codigos:
                codigo = input('Insira um Código de Barras valido: ')
            quantidade = getFloat('Informe a quantidade de produtos: ')
            valor_unitario = getFloat('Informe o valor unitário: ')
            Vendas(data, hora, cpf, codigo, quantidade, valor_unitario).cadastrar_venda()
        if acao2 == '2':
            listar_vendas()
            id_venda = getInt('Informe o id: ')
            Vendas(None, None, None, None, None, None).alterar_registro(id_venda)
        if acao2 == '3':
            listar_vendas()
            Vendas().excluir_registro(getInt('Informe o id: '))
        listar_vendas()
    elif acao in '4567':
        if acao == '4':
            acoes[acao](input('Informe o CPF: ').replace('-', '').replace('.', ''))
        elif acao == '5':
            acoes[acao](input('Informe o Código de Barras: '))
        else:
            acoes[acao]()
    conexao.commit()
    if input('Deseja parar? [S/N]\n').lower().startswith('s'):
        break

cursor.close()
conexao.close()
