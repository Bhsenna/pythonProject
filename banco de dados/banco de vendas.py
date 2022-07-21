import requests
import sqlite3
import validate_docbr as docbr
from operator import itemgetter
from Funções.Lista.Func import getInt
from Funções.Lista.Func import getFloat

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()


class Produto:
    def __init__(self, cod_barras, nome_produto, fabricante_produto):
        self.cob_barras = cod_barras
        self.nome_produto = nome_produto
        self.fabricante_produto = fabricante_produto

    def cadastrar_produto(self):
        cursor.execute('INSERT INTO produtos (cod_barras, nome_produto, fabricante_produto)'
                       'VALUES(?,?,?)', (self.cob_barras, self.nome_produto, self.fabricante_produto))

    def alterar_registro(self, id_produto):
        opcoes = ["cod_barras", "nome_produto", "fabricante_produto"]
        escolha = getInt('Você deseja alterar:\n[0] Código de Barras\n[1] Nome do Produto\n[2] Fabricante do Produto\n')
        novo_valor = [self.cob_barras, self.nome_produto, self.fabricante_produto]
        cursor.execute(f'UPDATE produtos SET {opcoes[escolha]}=? WHERE id_produto=?', (novo_valor[escolha], id_produto))

    @staticmethod
    def excluir_registro(id_produto):
        if input(f'Deseja deletar Produto? Essa ação é irreversível\n').lower() == 's':
            cursor.execute('DELETE FROM produtos WHERE id_produto=?', (id_produto,))
            print(f'Produto foi deletado')


class Cliente:
    def __init__(self, nome_cliente=None, cpf_cliente=None, cep_cliente=None):
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

    def alterar_registro(self, id_cliente):
        if self.validar_cpf():
            opcoes = ["nome_cliente", "cpf_cliente", "cep_cliente"]
            escolha = getInt('Você deseja alterar:\n[0] Nome do Cliente\n[1] CPF do Cliente\n[2] CEP do Cliente\n')
            novo_valor = [self.nome_cliente, self.cpf_cliente, self.cep_cliente]
            if escolha == 2:
                cursor.execute(f'UPDATE clientes SET cep_cliente=?, cidade_cliente=?, estado_cliente=?, rua_cliente=? WHERE "id cliente"=?',
                               (novo_valor[escolha], self.cidade_cliente, self.estado_cliente, self.rua_cliente, id_cliente))
            else:
                cursor.execute(f'UPDATE clientes SET {opcoes[escolha]}=? WHERE "id cliente"=?', (novo_valor[escolha], id_cliente))

    def excluir_registro(self, id_cliente):
        if self.validar_cpf():
            if input(f'Deseja deletar Cliente? Essa ação é irreversível\n').lower() == 's':
                cursor.execute('DELETE FROM clientes WHERE "id cliente"=?', (id_cliente,))
                print(f'Cliente foi deletado')


class Vendas:
    def __init__(self, data_venda, hora_venda, cpf_cliente, cod_barras, quantidade: float, valor_unitario: float):
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
        opcoes = ["data_venda", "hora_venda", "CPF_cliente", "cod_barras", "quantidade", "valor_unitario"]
        escolha = getInt('Você deseja alterar:\n[0] Data da Venda\n[1] Hora da Venda\n[2] CPF do Cliente\n[3] Código de Barras\n[4] Quantidade\n[5] Valor Unitário\n')
        novo_valor = [self.data_venda, self.hora_venda, self.cpf_cliente, self.cod_barras, self.quantidade, self.valor_unitario]
        cursor.execute(f'UPDATE vendas SET {opcoes[escolha]}=? WHERE id_venda=?', (novo_valor[escolha], id_venda))

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
        if acao2 in '123':
            codigo = input('Informe o Código de Barras: ')
            nome = input('Informe o Nome do Produto: ')
            fabricante = input('Informe o Fabricante: ')
        if acao2 == '1':
            Produto(codigo, nome, fabricante).cadastrar_produto()
        if acao2 == '2':
            Produto(codigo, nome, fabricante).alterar_registro(getInt('Informe o id: '))
        if acao2 == '3':
            Produto(codigo, nome, fabricante).excluir_registro(getInt('Informe o id: '))
    elif acao == '2':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 in '123':
            nome = input('Informe o Nome do Cliente: ')
            cpf = input('Informe o CPF fo Cliente: ')
            cep = input('Informe o CEP fo Cliente: ')
        if acao2 == '1':
            Cliente(nome, cpf, cep).cadastrar_cliente()
        if acao2 == '2':
            Cliente(nome, cpf, cep).alterar_registro(getInt('Informe o id: '))
        if acao2 == '3':
            Cliente(nome, cpf, cep).excluir_registro(getInt('Informe o id: '))
    elif acao == '3':
        acao2 = input('Você deseja:\n'
                      '[1] Cadastrar\n'
                      '[2] Alterar\n'
                      '[3] Excluir\n').strip()
        if acao2 in '123':
            data = input('Informe a Data da Venda: ')
            hora = input('Informe a Hora da Venda: ')
            cpf = input('Informe o CPF fo Cliente: ')
            codigo = input('Informe o Código de Barras: ')
            quantidade = getFloat('Informe a quantidade de produtos: ')
            valor_unitario = getFloat('Informe o valor unitário: ')
        if acao2 == '1':
            Vendas(data, hora, cpf, codigo, quantidade, valor_unitario).cadastrar_venda()
        if acao2 == '2':
            Vendas(data, hora, cpf, codigo, quantidade, valor_unitario).alterar_registro(getInt('Informe o id: '))
        if acao2 == '3':
            Vendas(data, hora, cpf, codigo, quantidade, valor_unitario).excluir_registro(getInt('Informe o id: '))
    elif acao in '4567':
        acoes[acao]()
    conexao.commit()
    if input('Deseja parar? ').lower() == 's':
        break

cursor.close()
conexao.close()