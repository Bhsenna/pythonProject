import sqlite3
from Funções.Lista.Func import getInt
from Funções.Lista.Func import getFloat
import pandas as pd
import arrow

pd.set_option('display.max_columns', 14)
pd.set_option('display.width', 400)

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
        print('Não há Aeronaves registradas')
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
        print('Não há Empresas registradas')
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
        print('Não há Aeroportos registrados')
    else:
        print(data_frame)


def listar_Voos():
    cursor.execute('SELECT * FROM Voos')
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
    for voo in cursor.fetchall():
        data['   Código'] += [voo[0]]
        data['   Data/Saída'] += [voo[1]]
        data['   Hora/Saída'] += [voo[2]]
        data['   Aeroporto Decolagem'] += [voo[3]]
        data['   Aeroporto Destino'] += [voo[4]]
        data['   Empresa'] += [voo[5]]
        data['   N° Passageiros'] += [voo[6]]
        data['   Assentos Disponíveis'] += [voo[7]]
        data['   Carga Carregada (Kg)'] += [voo[8]]
        data['   Aeronave'] += [voo[9]]
        data['   Data/Chegada'] += [voo[10]]
        data['   Hora/Chegada'] += [voo[11]]
        data['   Natureza Voo'] += [voo[12]]
    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há Voos registrados')
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
            cursor.execute('INSERT INTO Aeronaves (cod_aeronave, modelo, assentos_disponiveis, limite_bagagem)'
                           'VALUES(?,?,?,?)',
                           (self.cod_aeronave, self.modelo, self.assentos_disponiveis, self.limite_bagagem))
        except sqlite3.IntegrityError:
            print('\33[1;31mERRO:\33[0;31m Código de Aeronave já está cadastrado\33[0m\n')

    def alterar(self):
        opcoes = ["modelo", "assentos_disponiveis", "limite_bagagem"]
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
            print('\33[1;31mERRO:\33[0;31m Código de Empresa já está cadastrado\33[0m\n')

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
            print('\33[1;31mERRO:\33[0;31m Código de Aeroporto já está cadastrado\33[0m\n')

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
            cursor.execute('INSERT INTO Voos (cod_voo, data_saida, hora_saida, cod_aeroporto_decolagem, '
                           'cod_aeroporto_destino, cod_empresa, num_passageiros, assentos_disponiveis, '
                           'carga_carregada, cod_aeronave, data_chegada, hora_chegada, natureza_voo)'
                           'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                           (self.cod_voo, self.data_saida, self.hora_saida, self.cod_aeroporto_decolagem,
                            self.cod_aeroporto_destino, self.cod_empresa, self.num_passageiros,
                            self.assentos_disponiveis, self.carga_carregada, self.cod_aeronave,
                            self.data_chegada, self.hora_chegada, self.natureza_voo))
        except sqlite3.IntegrityError:
            print('\33[1;31mERRO:\33[0;31m Código de Voo já está cadastrado\33[0m\n')

    def alterar(self):
        opcoes = ["data_saida", "hora_saida", "cod_aeroporto_decolagem", "cod_aeroporto_destino",
                  "cod_empresa", "num_passageiros", "assentos_disponiveis", "carga_carregada",
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


def relatorio(opcao):
    data = {
        '   N° Passageiros': [],
        '   Assentos Disponíveis': [],
        '   Ocupação': [],
        '   Carga Carregada (Kg)': []
    }
    cursor.execute('SELECT * from Voos')
    if opcao == '1':
        data_inicio = input('Informe a primeira data (DD/MM/YYYY): ')
        data_inicio = int(data_inicio[6:] + data_inicio[3:5] + data_inicio[:2])
        data_final = input('Informe a segunda data (DD/MM/YYYY): ')
        data_final = int(data_final[6:] + data_final[3:5] + data_final[:2])
        if data_final < data_inicio:
            data_final, data_inicio = data_inicio, data_final
        for voo in cursor.fetchall():
            if data_inicio <= int(voo[1][6:] + voo[1][3:5] + voo[1][:2]) <= data_final:
                data['   N° Passageiros'] += [voo[6]]
                data['   Assentos Disponíveis'] += [voo[7]]
                data['   Carga Carregada (Kg)'] += [voo[8]]
                data['   Ocupação'] += [voo[6] / (voo[7]+voo[6])]

    elif opcao == '2':
        empresa = input('Informe o código da empresa: ')
        for voo in cursor.fetchall():
            if voo[5] == empresa:
                data['   N° Passageiros'] += [voo[6]]
                data['   Assentos Disponíveis'] += [voo[7]]
                data['   Carga Carregada (Kg)'] += [voo[8]]
                data['   Ocupação'] += [voo[6] / (voo[7] + voo[6])]

    elif opcao == '3':
        aeroporto = input('Informe o código do aeroporto: ')
        for voo in cursor.fetchall():
            if voo[3] == aeroporto or voo[4] == aeroporto:
                data['   N° Passageiros'] += [voo[6]]
                data['   Assentos Disponíveis'] += [voo[7]]
                data['   Carga Carregada (Kg)'] += [voo[8]]
                data['   Ocupação'] += [voo[6] / (voo[7] + voo[6])]

    data_frame = pd.DataFrame(data)
    if str(data_frame).startswith('Empty DataFrame'):
        print('Não há Voos registrados')
    else:
        print(data_frame)


dic1 = {'1': 'Aeronave', '2': 'Empresa', '3': 'Aeroporto', '4': 'Voo'}
while True:
    aeronaves = []
    cursor.execute('SELECT cod_aeronave FROM Aeronaves')
    for i in cursor.fetchall():
        aeronaves.append(i[0])
    aeroportos = []
    cursor.execute('SELECT cod_aeroporto FROM Aeroportos')
    for i in cursor.fetchall():
        aeroportos.append(i[0])
    empresas = []
    cursor.execute('SELECT cod_empresa FROM Empresas_Aereas')
    for i in cursor.fetchall():
        empresas.append(i[0])
    voos = []
    cursor.execute('SELECT cod_voo FROM Voos')
    for i in cursor.fetchall():
        voos.append(i[0])
    acao = input('Você deseja:\n'
                 '[1] Interagir com Aeronaves\n'
                 '[2] Interagir com Empresas\n'
                 '[3] Interagir com Aeroportos\n'
                 '[4] Interagir com Voos\n'
                 '[5] Ver relatório\n').strip()
    if acao in '1234':
        acao2 = input('Você deseja:\n'
                      f'[1] Cadastrar {dic1[acao]}\n'
                      f'[2] Editar {dic1[acao]}\n'
                      f'[3] Deletar {dic1[acao]}\n').strip()
    if acao == '1':  # Aeronave
        if acao2 == '1':  # Cadastrar
            codigo = input('Informe o código da Aeronave: ')
            modelo = input('Informe o modelo da Aeronave: ')
            assentos_disponiveis = getInt('Informe a quantidade de Assentos Disponíveis: ')
            limite_bagagem = getFloat('Informe o Limite de Bagagem (em Kg): ')
            Aeronaves(codigo, modelo, assentos_disponiveis, limite_bagagem).cadastrar()
        elif acao2 == '2':  # Editar
            listar_Aeronaves()
            codigo = input('Informe o Código da Aeronave que vai ser alterada: ')
            Aeronaves(codigo).alterar()
        elif acao2 == '3':  # Deletar
            listar_Aeronaves()
            codigo = input('Informe o Código da Aeronave que vai ser excluída: ')
            Aeronaves(codigo).excluir()
        listar_Aeronaves()
    elif acao == '2':  # Empresa
        if acao2 == '1':  # Cadastrar
            codigo = input('Informe o código da Empresa: ')
            nome = input('Informe o nome da Empresa: ')
            nacionalidade = input('Informe a nacionalidade da Empresa: ')
            sigla = input('Informe a sigla da Empresa: ')
            Empresas(codigo, nome, nacionalidade, sigla).cadastrar()
        elif acao2 == '2':  # Editar
            listar_Empresas()
            codigo = input('Informe o Código da Empresa que vai ser alterada: ')
            Empresas(codigo).alterar()
        elif acao2 == '3':  # Deletar
            listar_Empresas()
            codigo = input('Informe o Código da Empresa que vai ser excluída: ')
            Empresas(codigo).excluir()
        listar_Empresas()
    elif acao == '3':  # Aeroportos
        if acao2 == '1':  # Cadastrar
            codigo = input('Informe o código do Aeroporto: ')
            nome = input('Informe o nome do Aeroporto: ')
            sigla = input('Informe a sigla do Aeroporto: ')
            cidade = input('Informe a cidade do Aeroporto: ')
            estado = input('Informe o estado do Aeroporto: ')
            pais = input('Informe o país do Aeroporto: ')
            continente = input('Informe o continente do Aeroporto: ')
            Aeroportos(codigo, nome, sigla, cidade, estado, pais, continente).cadastrar()
        elif acao2 == '2':  # Editar
            listar_Aeroportos()
            codigo = input('Informe o Código do Aeroporto que vai ser alterado: ')
            Aeroportos(codigo).alterar()
        elif acao2 == '3':  # Deletar
            listar_Aeroportos()
            codigo = input('Informe o Código do Aeroporto que vai ser excluído: ')
            Aeroportos(codigo).excluir()
        listar_Aeroportos()
    elif acao == '4':  # Voos
        if acao2 == '1':  # Cadastrar
            codigo = input('Informe o código do Voo: ')
            data_saida = arrow.now().format('DD/MM/YYYY')
            hora_saida = arrow.now().format('HH:mm')
            codigo_aeroporto_decolagem = input('Informe o código do Aeroporto de Decolagem: ')
            while codigo_aeroporto_decolagem not in aeroportos:
                codigo_aeroporto_decolagem = input('Informe um código válido: ')
            codigo_aeroporto_destino = input('Informe o código do Aeroporto de Destino: ')
            while codigo_aeroporto_destino not in aeroportos:
                codigo_aeroporto_destino = input('Informe um código válido: ')
            codigo_empresa = input('Informe o código da Empresa: ')
            while codigo_empresa not in empresas:
                codigo_empresa = input('Informe um código válido: ')
            codigo_aeronave = input('Informe o código da Aeronave: ')
            while codigo_aeronave not in aeronaves:
                codigo_aeronave = input('Informe um código válido: ')
            assentos_max = cursor.execute('SELECT assentos_disponiveis FROM Aeronaves WHERE cod_aeronave=?', (codigo_aeronave,)).fetchall()[0][0]
            num_passageiros = getInt('Informe o número de passageiros: ')
            while num_passageiros > assentos_max:
                print(f'O número da passageiros excede a quantidade máxima de assentos! Esse avião suporta apenas {assentos_max} passageiros')
                num_passageiros = getInt('Informe o número de passageiros: ')
            assentos_disponiveis = assentos_max - num_passageiros
            limite = cursor.execute('SELECT limite_bagagem FROM Aeronaves WHERE cod_aeronave=?', (codigo_aeronave,)).fetchall()[0][0]
            carga_max = limite * num_passageiros
            carga_carregada = getFloat('Informe a carga total carregada pela Aeronave (em Kg): ')
            while carga_carregada > carga_max:
                print(f'O peso total excede o limite por passageiro! Cada passageiro só pode carregar {limite} kg, para um peso total de no máximo {carga_max} kg')
                carga_carregada = getFloat('Informe a carga total carregada pela Aeronave (em Kg): ')
            data_chegada = input('Informe a data de chegada (DD/MM/YYYY): ')
            hora_chegada = input('Informe a hora de chegada (HH:mm): ')
            natureza = input('Informe se o Voo é Nacional ou Internacional: ')
            Voos(codigo, data_saida, hora_saida, codigo_aeroporto_decolagem, codigo_aeroporto_destino, codigo_empresa, num_passageiros,
                 assentos_disponiveis, carga_carregada, codigo_aeronave, data_chegada, hora_chegada, natureza).cadastrar()
        elif acao2 == '2':  # Editar
            listar_Voos()
            codigo = input('Informe o Código do Voo que vai ser alterado: ')
            Voos(codigo).alterar()
        elif acao2 == '3':  # Deletar
            listar_Voos()
            codigo = input('Informe o Código do Voo que vai ser excluído: ')
            Voos(codigo).excluir()
        listar_Voos()
    elif acao == '5':
        filtro = input('Você deseja filtrar por:\n'
                       '[1] Período\n'
                       '[2] Empresa\n'
                       '[3] Aeroporto\n')
        relatorio(filtro)
    conexao.commit()
    if input('Deseja parar? [S/N]\n').lower().startswith('s'):
        break

cursor.close()
conexao.close()
