print('\x1b[38;5;3mOPERAÇÃO - SUBTRAÇÃO!'.center(25))
num = []
for i in range(3):
    print(25 * '=')
    print(f'Conta {i + 1}!\n'.center(25))
    novoNum1 = input('Digite um número: ')
    while type(novoNum1) != int:
        try:
            novoNum1 = int(novoNum1)
            num.append(novoNum1)
        except:
            print('Número inválido, tente novamente')
            novoNum1 = input('Digite um número: ')
    novoNum2 = input('Digite outro número: ')
    while type(novoNum2) != int:
        try:
            novoNum2 = int(novoNum2)
            num.append(novoNum2)
        except:
            print('Número inválido, tente novamente')
            novoNum2 = input('Digite outro número: ')
    print(f'\n{num[-2]} - {num[-1]} = {num[-2] - num[-1]}')