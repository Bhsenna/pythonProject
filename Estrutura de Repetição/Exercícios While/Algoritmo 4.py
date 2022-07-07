while True:
    numL = input('Insira os seus números: ').split()

    cont = 0
    while cont < len(numL):
        if numL[cont] == '0':
            numL.pop(cont)
        elif numL[cont].lstrip('-0').isnumeric():
            numL[cont] = int(numL[cont])
            cont += 1
        else:
            numL.pop(cont)

    cont, med = 0, 0
    while cont < len(numL):
        med += numL[cont]
        cont += 1
    if med % len(numL):
        med = f'{(med / len(numL)):.2f}'
    else:
        med = int(med / len(numL))
    print(f'\nA média aritmética dos seu números é {med}\n')

    cont, posL = 0, []
    while cont < len(numL):
        if numL[cont] > 0:
            posL.append(numL[cont])
        cont += 1
    print(f'A lista possui {len(posL)} valor(es) Positivo(s)')

    cont, negL = 0, []
    while cont < len(numL):
        if numL[cont] < 0:
            negL.append(numL[cont])
        cont += 1
    print(f'A lista possui {len(negL)} valor(es) Negativo(s)')

    print(f'A lista é {(len(negL) / len(numL) * 100):.2f}% valores Negativos, e {(len(posL) / len(numL) * 100):.2f}% valores Positivos')

    numL.sort()
    print(f'\nO menor valor é {numL[0]}, e o maior valor é {numL[len(numL) - 1]}')

    rep = input('\nQuer ver outra lista? (S ou N)\n').lower()
    if rep != 'S':
        break