contas, senhas = [500.00, 750.00, 1500.00], ["1234", "4321", "1423"]

opCon = input('Qual a sua conta? (1 - 3)\n').strip()
while opCon not in "123":
    print('Conta não encontrada, tente novamente')
    opCon = input('Qual a sua conta? (1 - 3)\n').strip()
opCon = int(opCon) - 1

opSen = input('Digite a Senha de 4 dígitos da sua Conta:\n').strip()
while not opSen.isnumeric() or len(opSen) != 4:
    print('Senha inválida, por favor digite apenas 4 números')
    opSen = input('Digite a Senha de 4 dígitos da sua Conta:\n').strip()
if opSen != senhas[opCon]:
    erros = 1
    while opSen != senhas[opCon]:
        opSen = input(f'Senha incorreta, tente novamente ({3 - erros} tentativas restantes)\n').strip()
        while not opSen.isnumeric() or len(opSen) != 4:
            print('Senha inválida, por favor digite apenas 4 números')
            opSen = input('Digite a Senha de 4 dígitos da sua Conta:\n').strip()
        erros += 1
        if erros == 3 and opSen != senhas[opCon]:
            print('Você errou vezes demais, sua conta foi bloqueada')
            exit()

sair = False
while not sair:
    opc = input("""O que desejas fazer?
a. Consultar Saldo
b. Pagar conta
c. Depositar na conta
d. Saque
e. Sair\n""").strip(' .').lower()
    while opc not in "abcde":
        print('Opção inválida, tente novamente')
        opc = input("""O que desejas fazer?
a. Consultar Saldo
b. Pagar conta
c. Depositar na conta
d. Saque
e. Sair\n""").strip(' .').lower()

    if opc == "a":
        print(f'O saldo da sua conta é R${contas[opCon]:.2f}')

    elif opc == "b":
        pag = input('Quanto você deve pagar?\nR$').strip()
        while not pag.replace(',', '').replace('.', '').isnumeric():
            print('Valor inválido, tente novamente')
            pag = input('Quanto você deve pagar?\nR$').strip()
        pag = float(pag.replace(',', '.'))
        if contas[opCon] - pag < 0:
            print('Você não tem saldo suficiente para pagar por isso')
        else:
            contas[opCon] = contas[opCon] - pag
            print(f'Pagamento concluído, seu novo saldo é R${contas[opCon]:.2f}')

    elif opc == "c":
        dep = input('Quanto você deseja depositar?\nR$').strip()
        while not dep.replace(',', '').replace('.', '').isnumeric():
            print('Valor inválido, tente novamente')
            dep = input('Quanto você deseja depositar?\nR$').strip()
        dep = float(dep.replace(',', '.'))
        contas[opCon] = contas[opCon] + dep
        print(f'Deposito concluído, seu novo saldo é RS{contas[opCon]:.2f}')

    elif opc == "d":
        saq = input('Quanto você deseja sacar?\nR$').strip()
        while not saq.replace(',', '').replace('.', '').isnumeric():
            print('Valor inválido, tente novamente')
            pag = input('Quanto você deseja sacar?\nR$').strip()
        saq = float(saq.replace(',', '.'))
        if contas[opCon] - saq < 0:
            print('Você não tem saldo suficiente para realizar esse saque')
        else:
            contas[opCon] = contas[opCon] - saq
            print(f'Saque concluído, seu novo saldo é R${contas[opCon]:.2f}')

    elif opc == "e":
        print('Até a próxima!')
        sair = True