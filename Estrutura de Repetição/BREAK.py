while True:
    cpf = list(input('Informe seu CPF: ').replace('.', '').replace('-', ''))
    i = 0
    while i <= 10:
        cpf[i] = int(cpf[i])
        i += 1

    if cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8] == cpf[9] == cpf[10]:
        print('Seu CPF é invalido, verifique sua identidade')
    else:

        ver1 = 11 - (((cpf[0] * 10) + (cpf[1] * 9) + (cpf[2] * 8) + (cpf[3] * 7) + (cpf[4] * 6) + (cpf[5] * 5) + (cpf[6] * 4) + (cpf[7] * 3) + (cpf[8] * 2)) % 11)
        if ver1 >= 10:
            ver1 = 0
        if ver1 == cpf[9]:

            ver2 = 11 - (((cpf[0] * 11) + (cpf[1] * 10) + (cpf[2] * 9) + (cpf[3] * 8) + (cpf[4] * 7) + (cpf[5] * 6) + (cpf[6] * 5) + (cpf[7] * 4) + (cpf[8] * 3) + (cpf[9] * 2)) % 11)
            if ver2 >= 10:
                ver2 = 0
            if ver2 == cpf[10]:
                print('Seu CPF é valido!')
                break
            else:
                print('Seu CPF é invalido, verifique sua identidade')
        else:
            print('Seu CPF é invalido, verifique sua identidade')