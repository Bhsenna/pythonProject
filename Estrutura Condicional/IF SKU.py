import sys
opc = int(input('Você gostaria de:\n(1) Registrar o código do seu produto\n(2) Ver as informações de um produto\n'))

if opc == 1:
    tipo = int(input('Selecione o seu produto:\n(1) Monitor\n(2) Teclado\n(3) Mouse\n'))
    if tipo == 1:
        tipo = 'MON'
    elif tipo == 2:
        tipo = 'TEC'
    elif tipo == 3:
        tipo = 'MOU'
    else:
        print('Informação inválida, tente novamente')
        sys.exit()

    cor = int(input('Selecione a cor:\n(1) Preto\n(2) Azul\n(3) Vermelho\n(4) Branco\n'))
    if cor == 1:
        cor = 'PR'
    elif cor == 2:
        cor = 'AZ'
    elif cor == 3:
        cor = 'VM'
    elif cor == 4:
        cor = 'BR'
    else:
        print('Informação inválida, tente novamente')
        sys.exit()

    mat = int(input('Selecione o material:\n(1) Polipropileno\n(2) Polietileno\n(3) Poliamida\n'))
    if mat == 1:
        mat = 'PP'
    elif mat == 2:
        mat = 'PE'
    elif mat == 3:
        mat = 'PO'
    else:
        print('Informação inválida, tente novamente')
        sys.exit()

    ger = int(input('Selecione a geração:\n(1) 1ª Geração\n(2) 2ª Geração\n(3) 3ª Geração\n'))
    if ger == 1:
        ger = '1G'
    elif ger == 2:
        ger = '2G'
    elif ger == 3:
        ger = '3G'
    else:
        print('Informação inválida, tente novamente')
        sys.exit()

    ano = input('Digite o Ano de Cadastro: ')

    print(f'Seu código é: {tipo}-{cor}-{mat}-{ger}/{ano}')

elif opc == 2:
    prod = input('Informe o código do seu produto: ').upper()

    if prod[0:3] == 'MON':
        tipo = 'Monitor'
    elif prod[0:3] == 'TEC':
        tipo = 'Teclado'
    elif prod[0:3] == 'MOU':
        tipo = 'Mouse'
    else:
        print('Código inválido, tente novamente')
        sys.exit()

    if prod[4:6] == 'PR':
        cor = 'Preto'
    elif prod[4:6] == 'AZ':
        cor = 'Azul'
    elif prod[4:6] == 'VM':
        cor = 'Vermelho'
    elif prod[4:6] == 'BR':
        cor = 'Branco'
    else:
        print('Código inválido, tente novamente')
        sys.exit()

    if prod[7:9] == 'PP':
        mat = 'Polipropileno'
    elif prod[7:9] == 'PE':
        mat = 'Polietileno'
    elif prod[7:9] == 'PO':
        mat = 'Poliamida'
    else:
        print('Código inválido, tente novamente')
        sys.exit()

    if prod[10:12] == '1G':
        ger = '1ª Geração'
    elif prod[10:12] == '2G':
        ger = '2ª Geração'
    elif prod[10:12] == '3G':
        ger = '3ª Geração'
    else:
        print('Código inválido, tente novamente')
        sys.exit()

    ano = prod[13:50]

    print(f'''Informações:
Tipo: {tipo}
Cor: {cor}
Material: {mat}
Geração: {ger}
Ano de Registro: {ano}''')